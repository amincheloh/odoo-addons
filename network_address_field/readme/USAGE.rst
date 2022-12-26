To use this module, you need to use like this::

    from odoo import fields, models


    class YourModel(models.Model):

        ip = fields.IPv4Host(string="IP", tracking=True)
        network = fields.IPv4Network(string="Network", tracking=True)
