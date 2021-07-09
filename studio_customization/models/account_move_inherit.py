from odoo import models, fields, api

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    bill_reference_number = fields.Char(
        string='Bill Reference Number',
        required=False)

    customer_notes = fields.Text(
        string="Customer Notes",
        required=False,readonly=True)

    customer_po = fields.Char(
        string='Customer Po#',
        required=False)

    field_OQDvV = fields.Text(
        string="New Related Field",
        required=False, readonly= True)

    field_t1owR = fields.Char(
        string='Customer po #',
        required=False)

    field_tXAja = fields.Char(
        string='New Text',
        required=False)

    po_number = fields.Char(
        string='PO Number',
        required=False)

    sales_order_number = fields.Char(
        string='Sale Order Number',
        required=False)

    term = fields.Char(
        string='Term',
        required=False)

    global_comments = fields.Text(
        string="Global Comments",
        required=False)

    comments_invoice = fields.Text(
        string="Invoice Notes",
        required=False)

    delievery_method = fields.Selection(
        string='Delievery Method',
        selection=[('SATURDAY DELIVERY', 'SATURDAY DELIVERY'),
                   ('PUROLATOR', 'PUROLATOR'),
                   ('UPS', 'UPS'), ],
        required=False, )

    warehouse_note = fields.Text(
        string="Warehouse Note",
        required=False)



class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    invoice_count = fields.Integer(
        string='Invoice Count',
        required=False,readonly=True,copy=True)

    qty_Delivered = fields.Float(
        string='Qty Delivered',
        required=False,readonly=True)

    qty_ordered = fields.Float(
        string=' Qty Ordered',
        required=False,readonly=True,copy=True)

    bill_count = fields.Integer(
        string=' Bill Count',
        required=False,readonly=True)

    cost = fields.Float(
        string='Cost',
        required=False,readonly=True)

    field_76kO1 = fields.Char(
        string='Field 76kO1',
        required=False)

    field_hjhZ3 = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    field_mY2ct = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    notes = fields.Char(
        string='Note',
        required=False,)

    notes_1 = fields.Char(
        string='Notes',
        required=False)

    purchases_qty_received_accumulate = fields.Float(
        string='Purchases Qty Received Accumulate',
        required=False,readonly=True)

    qty_bo= fields.Float(
        string='Qty BO',
        required=False,readonly=True,compute='_compute_qty_bo')

    qty_bo_po = fields.Float(
        string='Qty BO',
        required=False,readonly=True,compute='_compute_qty_bo_po')

    qty_ordered = fields.Float(
        string='Qty Ordered',
        required=False,readonly=True,compute='_compute_qty_ordered_')

    qty_ordered_good_1 = fields.Float(
        string=' Qty Ordered',
        required=False,readonly=True,compute='_compute_qty_ordered_good_1_')

    qty_ordered_original = fields.Float(
        string=' Qty Ordered Original',
        required=False,readonly=True)

    serial_number = fields.Text(
        string="Serial Number",
        required=False,compute='_compute_serial_number')

    unit_price_after= fields.Monetary(
        string="Unit Price After",
        required=False,readonly=True, compute='_compute_unit_price_after'
    )

    move_type = fields.Selection(
        string='Type',
        selection=[
            ('entry', 'Journal Entry'),
            ('out_invoice', 'Customer Invoice'),
            ('out_refund', 'Customer Credit Note'),
            ('in_invoice', 'Vendor Bill'),
            ('in_refund', 'Vendor Credit Note'),
            ('out_receipt', 'Sales Receipt'),
            ('in_receipt', 'Purchase Receipt'),
        ],
        required=False,related='move_id.move_type')

    purchase_id = fields.Many2one(
        comodel_name='purchase.order',
        string=' purchase_id',
        required=False,related='purchase_line_id.order_id')

    tax_ids = fields.Many2many(
        comodel_name='account.tax',
        string='Tax ids')

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account',
        required=False,related='move_id.company_id')


    @api.depends('price_subtotal')
    def _compute_unit_price_after(self):
        for record in self:
            if record.quantity == 0:
                record[("unit_price_after")] = record.price_unit
            elif record.quantity != 0:
                record[("unit_price_after")] = record.price_subtotal / record.quantity


    @api.depends('reconciliation_invoice_id')
    def _compute_serial_number(self):
        re = ''
        for record in self:
            move_line_ids = record.mapped('sale_line_ids').mapped('move_ids').mapped('move_line_ids')

            for move_line_id in move_line_ids:
                if str(move_line_id.lot_id.name) == "False":
                    re = " "
                else:
                    re += 'S/N: ' + str(move_line_id.lot_id.name) + ', '

            record['serial_number'] = re
            re = ''


    @api.depends('qty_ordered')
    def _compute_qty_ordered_good_1_(self):
        for record in self:
            if record.invoice_count == 1:
                record['qty_ordered_good_1'] = record.qty_ordered
            elif record.invoice_count > 1:
                record['qty_ordered_good_1'] = (record.qty_ordered - record.qty_Delivered) + record.quantity
            else:
                record.qty_ordered_good_1 = 0

    @api.depends('quantity')
    def _compute_qty_ordered_(self):
        for record in self:
            if record.bill_count == 0:
                record['qty_ordered'] = record.qty_ordered_original
            elif record.bill_count >= 1:
                record['qty_ordered'] = record.qty_ordered_original - record.purchases_qty_received_accumulate + record.quantity

    @api.depends('quantity')
    def _compute_qty_bo_po(self):
        for record in self:
            if record.bill_count == 0:
                record['qty_bo_po'] = record.qty_ordered_original
            elif record.bill_count >= 1:
                record['qty_bo_po'] = record.qty_ordered - record.quantity

    @api.depends('quantity')
    def _compute_qty_bo(self):
        for record in self:
            if record.invoice_count == 1:
                record['qty_bo'] = record.qty_ordered - record.quantity
            else:
                record['qty_bo'] = record.qty_ordered_good_1 - record.quantity
