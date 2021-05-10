# -*- coding: utf-8 -*-
# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_order_confirmation_email_ids = fields.Many2many(
        'res.partner', readonly=False, string="Account Tags")
