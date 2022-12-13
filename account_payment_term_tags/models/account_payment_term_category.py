# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from random import randint

from odoo import fields, models


class AccountPaymentTermCategory(models.Model):
    _name = "account.payment.term.category"
    _description = "Account Payment Term Category"

    def _get_default_color(self):
        return randint(1, 11)

    active = fields.Boolean(default=True)
    name = fields.Char(string="Tag Name", required=True, translate=True)
    color = fields.Integer(default=_get_default_color)
    payment_term_ids = fields.Many2many(
        "account.payment.term",
        "account_payment_term_category_rel",
        "category_id",
        "payment_id",
        string="Payments",
    )

    _sql_constraints = [
        ("name_uniq", "unique (name)", "Tag name already exists !"),
    ]
