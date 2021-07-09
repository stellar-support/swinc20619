from odoo import models, fields, api


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=False, related="purchase_id.currency_id")

    customer_po_onPickSlip = fields.Char(
        string='Customer PO #',
        required=False, related="sale_id.customer_po_")

    invoice_number = fields.Text(
        string="Invoice Number",
        required=False, related="purchase_id.invoice")

    stage_id = fields.Many2one(
        comodel_name='stock.picking.stage',
        string='stage id',
        required=False)

    argo_reference = fields.Text(
        string="Argo Reference #",
        required=False)

    bill_reference_ = fields.Char(
        string='Bill Reference #',
        required=False, related="purchase_id.bill_reference_")

    delivery_method = fields.Selection(
        string='Delivery Method',
        selection=	[['Saturday Delivery', 'Saturday Delivery'], ['Purolator', 'Purolator'], ['UPS', 'UPS']],
        required=False, related="sale_id.delivery_method")

    field_FRcQD = fields.Monetary(
        string='PO Total',
        required=False, related="purchase_id.amount_total")

    field_pw11C = fields.Char(
        string='New Related Field',
        required=False,readonly=True, related="sale_id.customer_po_")

    global_comments = fields.Text(
        string="Global Comments",
        required=False, related="sale_id.comments_1")

    operation_type = fields.Char(
        string='Operation Type',
        required=False,readonly=True, related="picking_type_id.name")

    operation_type_id = fields.Integer(
        string='Operation Type ID',
        required=False,readonly=True, related="picking_type_id.id")

    pink_slip = fields.Text(
        string="Pink slip #",
        required=False)

    po_ = fields.Char(
        string='PO #',
        required=False,readonly=True, related="purchase_id.po_")

    po_taxes = fields.Monetary(
        string = "PO Taxes",readonly=True, related="purchase_id.amount_tax"
    )

    purchase_stellar_status = fields.Char(
        string='Purchase stellar status',
        required=False,readonly=True, related="purchase_id.purchase_stellar_status")

    so_ = fields.Text(
        string="SO #",
        required=False, related="purchase_id.so")

    stage = fields.Char(
        string='Stage',
        required=False, related="stage_id.display_name")

    stellar_status_picking = fields.Char(
        string='Stellar Status Picking',
        required=False,readonly=True, related="sale_id.status_stellar")

    type_of_operation = fields.Selection(
        string='Type of operation',
        selection=[['incoming', 'Vendors'], ['outgoing', 'Customers'], ['internal', 'Internal']],
        required=False,readonly=True, related="picking_type_id.code")

    untaxes_amount= fields.Monetary(
        string="Untaxes Amount",
        readonly=True, related="purchase_id.amount_untaxed"
    )

    warehouse_notes_1 = fields.Text(
        string="Warehouse notes 1",
        required=False, related="sale_id.note")

        
