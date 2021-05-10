# -*- coding: utf-8 -*-
# Copyright 2021 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_order_confirmation_email_ids = fields.Many2many(
        related="company_id.sale_order_confirmation_email_ids", readonly=False, string="Account Tags")
    send_sale_confirmation_email = fields.Boolean(default=True)
