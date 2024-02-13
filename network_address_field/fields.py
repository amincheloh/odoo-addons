import ipaddress

from odoo import _, fields


class NetworkAddressField(fields.Field):
    def convert_to_record(self, value, record):
        return value if value else None


class IPv4Host(NetworkAddressField):
    type = "ipv4_host"

    column_type = ("inet", "inet")

    def convert_to_column(self, value, record, values=None, validate=True):
        ip_str = str(value)
        if value and validate:
            try:
                ip = ipaddress.ip_interface(ip_str)
                if ip.version != 4:
                    raise ValueError()
                return ip.with_prefixlen
            except ValueError as err:
                raise ValueError(
                    _("%(value)s does not appear to be an IPv4 address", value=ip_str)
                ) from err

        return ip_str if value else None

    @staticmethod
    def to_ipaddress(value):
        if not value:
            return None

        return ipaddress.ip_interface(value)

    @staticmethod
    def to_string(value):
        if not value:
            return None

        if isinstance(value, str):
            value = IPv4Host.to_ipaddress(value)
        return str(value.ip) if value.network.prefixlen == 32 else str(value)

    def convert_to_cache(self, value, record, validate=True):
        return self.to_ipaddress(value)

    def convert_to_record(self, value, record):
        return self.to_ipaddress(value)

    def convert_to_read(self, value, record, use_name_get=True):
        return self.to_string(value)

    def convert_to_export(self, value, record):
        return self.to_string(value)


class IPv4Network(NetworkAddressField):
    type = "ipv4_network"

    column_type = ("cidr", "cidr")

    def convert_to_column(self, value, record, values=None, validate=True):
        network_str = str(value)
        if value and validate:
            try:
                network = ipaddress.ip_network(network_str)
                if network.version != 4:
                    raise ValueError()
            except ValueError as err:
                raise ValueError(
                    _(
                        "%(value)s does not appear to be an IPv4 Network",
                        value=network_str,
                    )
                ) from err

        return network_str if value else None

    @staticmethod
    def to_ipaddress(value):
        if not value:
            return None

        return ipaddress.ip_network(value)

    @staticmethod
    def to_string(value):
        if not value:
            return None

        if isinstance(value, str):
            value = IPv4Host.to_ipaddress(value)
        return str(value)

    def convert_to_cache(self, value, record, validate=True):
        return self.to_ipaddress(value)

    def convert_to_record(self, value, record):
        return self.to_ipaddress(value)

    def convert_to_read(self, value, record, use_name_get=True):
        return self.to_string(value)

    def convert_to_export(self, value, record):
        return self.to_string(value)


fields.IPv4Host = IPv4Host
fields.IPv4Network = IPv4Network
