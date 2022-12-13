# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Payment Term Tags",
    "summary": "Tags/Categories field for Account Payment Term",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Amin Cheloh",
    "website": "https://github.com/amincheloh/odoo-addons",
    "category": "Accounting/Accounting",
    "depends": ["account"],
    "images": ["static/description/cover.png"],
    "data": [
        "security/account_payment_term_category_security.xml",
        "views/account_payment_term_category_views.xml",
        "views/account_payment_term_views.xml",
    ],
}
