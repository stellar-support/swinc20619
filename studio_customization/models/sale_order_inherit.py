from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    argo_so = fields.Char(
        string='Argo SO #',
        required=False)

    comment_1 = fields.Text(
        string="Global Comments",
        required=False)

    customer_notes = fields.Text(
        string="Customer Notes",
        required=False, readonly=True)

    customer_po_ = fields.Char(
        string='Customer Po #',
        required=False)

    delivery_method = fields.Selection(
        string='Delivery_method',
        selection=[('SATURDAY DELIVERY', 'SATURDAY DELIVERY'),
                   ('PUROLATOR', 'PUROLATOR'),
                   ('UPS', 'UPS'), ],
        required=False,)

    YR61u = fields.Integer(
        string='Invoice Count to Update',
        required=False, readonly=True)

    status_stellar = fields.Char(
        string='Status stellar',
        required=False,readonly=True,copy=True)

    website_status_1 = fields.Char(
        string='Website Status',
        required=False)

class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    A6aTY = fields.Char(
        string='Product Note',
        required=False)

    FnedJ = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    Q61lY = fields.Char(
        string='New Text',
        required=False,readonly=True)

    XsiJW = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    invoice_count = fields.Integer(
        string='Invoice Count',
        required=False,readonly=True)

    notes = fields.Char(
        string='New Text',
        required=False)

    sku = fields.Char(
        string='Sku',
        required=False,readonly=True)

    stellar_status = fields.Char(
        string='Stellar status',
        required=False,readonly=True)

    unit_price_after_discount=fields.Monetary(
        string='Unit price After Discount Fields',
        required=False,readonly=True,compute='compute_price_after_discount')

    unit_price_discount=fields.Monetary(
        string='Unit price Discount',
        required=False, readonly=True, compute='compute_price_discount'
    )

    vendor = fields.Char(
        string='Vendor',
        required=False,readonly=True)

    vendor_1 = fields.Char(
        string='Vendor',
        required=False, readonly=True)

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


