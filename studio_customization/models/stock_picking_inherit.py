from odoo import models, fields, api


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=False)

    customer_po_onPickSlip = fields.Char(
        string='Customer PO #',
        required=False)

    invoice_number = fields.Text(
        string="Invoice Number",
        required=False)

    stage_id = fields.Many2one(
        comodel_name='stock.picking.stage',
        string='stage id',
        required=False)

    argo_reference = fields.Text(
        string="Argo Reference #",
        required=False)

    bill_reference_ = fields.Char(
        string='Bill Reference #',
        required=False)

    delivery_method = fields.Selection(
        string='Delivery Method',
        selection=	[['Saturday Delivery', 'Saturday Delivery'], ['Purolator', 'Purolator'], ['UPS', 'UPS']],
        required=False)

    field_FRcQD = fields.Monetary(
        string='PO Total',
        required=False)

    field_pw11C = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    global_comments = fields.Text(
        string="Global Comments",
        required=False)

    operation_type = fields.Char(
        string='Operation Type',
        required=False,readonly=True)

    operation_type_id = fields.Integer(
        string='Operation Type ID',
        required=False,readonly=True)

    pink_slip = fields.Text(
        string="Pink slip #",
        required=False)

    po_ = fields.Char(
        string='PO #',
        required=False,readonly=True)

    po_taxes = fields.Monetary(
        string = "PO Taxes",readonly=True
    )

    purchase_stellar_status = fields.Char(
        string='Purchase stellar status',
        required=False,readonly=True)

    so_ = fields.Text(
        string="SO #",
        required=False)

    stage = fields.Char(
        string='Stage',
        required=False)

    stellar_status_picking = fields.Char(
        string='Stellar Status Picking',
        required=False,readonly=True)

    type_of_operation = fields.Selection(
        string='Type of operation',
        selection=[['incoming', 'Vendors'], ['outgoing', 'Customers'], ['internal', 'Internal']],
        required=False,readonly=True)

    untaxes_amount= fields.Monetary(
        string="Untaxes Amount",
        readonly=True
    )

    warehouse_notes_1 = fields.Text(
        string="Warehouse notes 1",
        required=False)

        
