# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Network Address Field",
    "summary": "Network Address Fields and Widgets",
    "version": "16.0.1.0.2",
    "license": "AGPL-3",
    "author": "Amin Cheloh",
    "website": "https://github.com/amincheloh/odoo-addons",
    "depends": ["base", "web", "mail"],
    "category": "Hidden",
    "assets": {
        "web.assets_backend": [
            "network_address_field/static/src/views/fields/ipv4_field.esm.js",
            "network_address_field/static/src/views/fields/ipv4_field.xml",
            "network_address_field/static/src/views/fields/ipv4_field.scss",
        ],
    },
}
