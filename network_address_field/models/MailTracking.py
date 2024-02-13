from odoo import api, fields, models


class MailTracking(models.Model):
    _inherit = "mail.tracking.value"

    @api.model
    def create_tracking_values(
        self,
        initial_value,
        new_value,
        col_name,
        col_info,
        tracking_sequence,
        model_name,
    ):
        field = self.env["ir.model.fields"]._get(model_name, col_name)
        if not field:
            return

        if col_info["type"] in ["ipv4_host", "ipv4_network"]:
            return {
                "field": field.id,
                "field_desc": col_info["string"],
                "field_type": col_info["type"],
                "tracking_sequence": tracking_sequence,
                "old_value_char": fields.IPv4Host.to_string(initial_value)
                if col_info["type"] == "ipv4_host"
                else initial_value,
                "new_value_char": fields.IPv4Host.to_string(new_value)
                if col_info["type"] == "ipv4_host"
                else new_value,
            }

        return super().create_tracking_values(
            initial_value, new_value, col_name, col_info, tracking_sequence, model_name
        )
