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