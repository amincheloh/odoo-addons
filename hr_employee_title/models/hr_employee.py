# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        self.related_contact_ids.title = self.title
        return res

    def write(self, vals):
        res = super().write(vals)
        self.related_contact_ids.title = self.title
        return res
