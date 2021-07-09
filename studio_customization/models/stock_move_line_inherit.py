from odoo import models, fields, api

class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=False)

    admin_notes = fields.Char(
        string='Admin Notes',
        required=False)

    customer_name = fields.Char(
        string='Customer Name',
        required=False,readonly=True)

    customer_name_1 = fields.Many2one(
        comodel_name='res.partner',
        string='Customer Name',
        required=False,readonly=True)

    invoice_date = fields.Date(
        string='Invoice Date',
        required=False,readonly=True)

    invoice_number = fields.Char(
        string='Invoice Number',
        required=False,readonly=True)

    item_number = fields.Char(
        string='Item Number',
        required=False,readonly=True)

    notes = fields.Char(
        string='Notes',
        required=False)

    ordered_qty = fields.Float(
        string='Ordered Qty',
        required=False,readonly=True)

    product_name = fields.Char(
        string='Product Name',
        required=False,readonly=True)

    rma_customer_number = fields.Char(
        string='Rma Customer Number',
        required=False)

    rma_request_type = fields.Selection(
        string='RMA Request Type',
        selection = [["Refund","Refund"],["Replace","Replace"],["Repair","Repair"]],
        required=False)

    subtotal = fields.Monetary(
        string='Subtotal',
        required=False,readonly=True)

    unit_price = fields.Monetary(
        string='Unit Price',
        required=False, readonly=True)

    unit_price_1 = fields.Monetary(
        string='Unit Price',
        required=False, readonly=True)

    vendor_name = fields.Char(
        string='Vendor Name',
        required=False,readonly=True)

    unit_price_after_discount = fields.Monetary(
        string='Unit Price After Discount',
        required=False, readonly=True)


