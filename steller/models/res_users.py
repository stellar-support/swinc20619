# Copyright 2021 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    subscribed_to_confirmation_email = fields.Boolean(
        related="partner_id.subscribed_to_confirmation_email",
        readonly=False
    )
