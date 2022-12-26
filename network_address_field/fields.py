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

    def convert_to_cache(self, value, record, validate=True):
        if not value:
            return None

        return ipaddress.ip_interface(value)

    def convert_to_record(self, value, record):
        if not value:
            return None

        return ipaddress.ip_interface(value)


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

    def convert_to_cache(self, value, record, validate=True):
        if not value:
            return None

        return ipaddress.ip_network(value)

    def convert_to_record(self, value, record):
        if not value:
            return None

        return ipaddress.ip_network(value)


fields.IPv4Host = IPv4Host
fields.IPv4Network = IPv4Network
