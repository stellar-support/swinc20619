from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    argo_so = fields.Char(
        string='Argo SO #',
        required=False)

    comments_1 = fields.Text(
        string="Global Comments",
        required=False)

    customer_notes = fields.Text(
        string="Customer Notes",
        required=False, readonly=True, related="partner_id.comment")

    customer_po_ = fields.Char(
        string='Customer Po #',
        required=False)

    delivery_method = fields.Selection(
        string='Delivery_method',
        selection=[('SATURDAY DELIVERY', 'SATURDAY DELIVERY'),
                   ('PUROLATOR', 'PUROLATOR'),
                   ('UPS', 'UPS'), ],
        required=False,)

    field_YR61u = fields.Integer(
        string='Invoice Count to Update',
        required=False, readonly=True, related="invoice_count")

    status_stellar = fields.Char(
        string='Status stellar',
        required=False,readonly=True,copy=True)

    website_status_1 = fields.Char(
        string='Website Status',
        required=False)

    partner_note = fields.Text('Client Notes', help="Notes entered by the client at checkout")

    def action_confirm_stellar(self):
        self.update_shipping_address()
        # Only orders from a website
        for order in self.filtered('website_id'):
            order.send_sale_order_confirmation_email()

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


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    field_A6aTY = fields.Char(
        string='Product Note',
        required=False)

    field_FnedJ = fields.Char(
        string='New Related Field',
        required=False,readonly=True, related="product_id.seller_ids.company_id.name")

    field_Q61lY = fields.Char(
        string='New Text',
        required=False,readonly=True, related="product_id.seller_ids.display_name")

    field_XsiJW = fields.Char(
        string='New Related Field',
        required=False,readonly=True, related="product_id.seller_ids.display_name")

    invoice_count = fields.Integer(
        string='Invoice Count',
        required=False,readonly=True, related="order_id.invoice_count")

    notes = fields.Char(
        string='New Text',
        required=False)

    sku = fields.Char(
        string='Sku',
        required=False,readonly=True, related="product_id.default_code")

    stellar_status = fields.Char(
        string='Stellar status',
        required=False,readonly=True, related="order_id.status_stellar")

    unit_price_after_discount=fields.Monetary(
        string='Unit price After Discount Fields',
        required=False,readonly=True,compute='compute_price_after_discount')

    unit_price_discount=fields.Monetary(
        string='Unit price Discount',
        required=False, readonly=True, compute='compute_price_discount'
    )

    vendor = fields.Char(
        string='Vendor',
        required=False,readonly=True, related="product_id.seller_ids.display_name")

    vendor_1 = fields.Char(
        string='Vendor',
        required=False, readonly=True, related="product_id.seller_ids.display_name")

    @api.depends('price_subtotal')
    def compute_price_discount(self):
        for record in self:
            record[("unit_price_discount")] = (record.price_unit * record.discount) / 100


    @api.depends('price_subtotal')
    def compute_price_after_discount(self):
        for record in self:
            if record.product_uom_qty == 0:
                record[("unit_price_after_discount")] = record.price_unit
            else:
                record[("unit_price_after_discount")] = record.price_subtotal / record.product_uom_qty


