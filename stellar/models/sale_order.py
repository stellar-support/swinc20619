# -*- coding: utf-8 -*-
# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        super().action_confirm()
        if self.team_id.name == 'Online':
            self.sale_order_confirmation_email()

    def sale_order_confirmation_email(self):
        test_partner = self.env['res.partner'].search([('email', '=', 'yoany@vauxoo.com')])
        partner_email_ids = self.company_id.sale_order_confirmation_email_ids
        template = self.env.ref('stellar.email_sale_order_confirmation')
        for partner in partner_email_ids:
            template.with_context(partner_id=test_partner.id).send_mail(
                self.id, force_send=True, email_values={'email_to': '%s <%s>' % (partner.name, partner.email),})
