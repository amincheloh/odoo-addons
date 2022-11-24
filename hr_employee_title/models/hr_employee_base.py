# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    title = fields.Many2one("res.partner.title")
