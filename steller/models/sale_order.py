# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_note = fields.Text('Client Notes', help="Notes entered by the client at checkout")

    @api.multi
    def action_confirm_stellar(self):
        self.update_shipping_address()
        # Only orders from a website
        for order in self.filtered('website_id'):
            order.send_sale_order_confirmation_email()

    @api.multi
    def update_shipping_address(self):
        for order in self:
            # Verify that the order has delivery and this delivery is selected to pick up at the warehouse
            if not order.has_delivery or not order.carrier_id.pickup_warehouse:
                order.reset_shipping_address()
                continue
            warehouse = order.carrier_id.warehouse_id
            # Verify if a warehouse is selected and this warehouse has an address
            if not warehouse or not warehouse.partner_id:
                order.reset_shipping_address()
                continue
            # res.partner(1) fails, so we set his child
            order.partner_shipping_id = (warehouse.partner_id.child_ids[:1] or warehouse.partner_id).id

    def reset_shipping_address(self):
        """The shipping address of an order is the shipping address of the last purchase,
        so if you bought with pick up in the warehouse, the new orders will have the warehouse
        address instead of the customer's address."""
        shippings = self.partner_id.search([
            ("id", "child_of", self.partner_id.commercial_partner_id.ids),
            '|', ("type", "in", ["delivery", "other"]), ("id", "=", self.partner_id.commercial_partner_id.id)
        ]) | self.partner_id | self.partner_id.child_ids

        if self.partner_shipping_id.id not in shippings.ids:
            self.partner_shipping_id = self.partner_id.id

    def send_sale_order_confirmation_email(self):
        self.ensure_one()
        partner_email_ids = self.website_id.salesteam_id.member_ids.filtered(
            lambda member: member.subscribed_to_confirmation_email and member.email).mapped('partner_id')
        template = self.env.ref('stellar.email_sale_order_confirmation')
        for partner in partner_email_ids:
            template.with_context(partner_id=partner.id).send_mail(
                self.id, force_send=True, email_values={'email_to': '%s <%s>' % (partner.name, partner.email), })
