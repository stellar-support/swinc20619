# Copyright 2021 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    subscribed_to_confirmation_email = fields.Boolean(
        'Subscribed to sale order confirmation email',
        help="""Any user whose form part of a sales team and has this
                field checked will receive an email when a sale order is confirmed""")
