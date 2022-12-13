# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    category_ids = fields.Many2many(
        "account.payment.term.category",
        "account_payment_term_category_rel",
        "payment_id",
        "category_id",
        string="Tags",
    )
