from odoo import api, fields, models


class IrFieldsConverter(models.AbstractModel):
    _inherit = "ir.fields.converter"

    @api.model
    def _str_to_ipv4_host(self, model, field, value):
        parsed = fields.IPv4Host.to_ipaddress(value)
        return fields.IPv4Host.to_string(parsed), []

    @api.model
    def _str_to_ipv4_network(self, model, field, value):
        parsed = fields.IPv4Network.to_ipaddress(value)
        return fields.IPv4Network.to_string(parsed), []
