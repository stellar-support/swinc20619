from odoo import models, fields, api

class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=False)

    admin_notes = fields.Char(
        string='Admin Notes',
        required=False, related="picking_id.partner_id.name")

    customer_name = fields.Char(
        string='Customer Name',
        required=False,readonly=True)

    customer_name_1 = fields.Many2one(
        comodel_name='res.partner',
        string='Customer Name',
        required=False,readonly=True, related="picking_id.sale_id.partner_id")

    invoice_date = fields.Date(
        string='Invoice Date',
        required=False,readonly=True, related="picking_id.sale_id.invoice_ids.date")

    invoice_number = fields.Char(
        string='Invoice Number',
        required=False,readonly=True)

    item_number = fields.Char(
        string='Item Number',
        required=False,readonly=True, related="move_id.product_id.default_code")

    notes = fields.Char(
        string='Notes',
        required=False)

    ordered_qty = fields.Float(
        string='Ordered Qty',
        required=False,readonly=True, related="move_id.sale_line_id.product_uom_qty")

    product_name = fields.Char(
        string='Product Name',
        required=False,readonly=True, related="move_id.product_id.name")

    rma_customer_number = fields.Char(
        string='Rma Customer Number',
        required=False)

    rma_request_type = fields.Selection(
        string='RMA Request Type',
        selection = [["Refund","Refund"],["Replace","Replace"],["Repair","Repair"]],
        required=False)

    subtotal = fields.Monetary(
        string='Subtotal',
        required=False,readonly=True, related="move_id.sale_line_id.price_subtotal")

    unit_price = fields.Monetary(
        string='Unit Price',
        required=False, readonly=True, related="move_id.sale_line_id.unit_price_discount")

    unit_price_1 = fields.Monetary(
        string='Unit Price',
        required=False, readonly=True, related="picking_id.sale_id.invoice_ids.invoice_line_ids.unit_price_after")

    vendor_name = fields.Char(
        string='Vendor Name',
        required=False,readonly=True, related="product_id.vendor_name")

    unit_price_after_discount = fields.Monetary(
        string='Unit Price After Discount',
        required=False, readonly=True, related="move_id.sale_line_id.unit_price_after_discount")

