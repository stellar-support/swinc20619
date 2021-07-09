# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    picking_count_1 = fields.Integer(
        string='Picking Count',
        required=False,readonly=True, related="picking_count")

    purchase_stellar_status = fields.Char(
        string='Stellar Status',
        required=False,copy=True)

    bill_reference_ = fields.Char(
        string='Bill Reference #',
        required=False)

    comments_po = fields.Text(
        string="Comments",
        required=False)

    deliver_to_address = fields.Many2one(
        comodel_name='res.partner',
        string='Deliver To Address',
        required=False,domain="[('customer','=',True)]")

    invoice = fields.Text(
        string="Invoice #",
        required=False)

    po_ = fields.Char(
        string='Po #',
        required=False)

    select_broker_1 = fields.Selection(
        string='Select Broker',
        selection=[["WILLSON INTERNATIONAL 1-800-871-1918 cdnpars@willsonintl.com"
                       ,"US - WILLSON INTERNATIONAL 1-800-871-1918 cdnpars@willsonintl.com"]
            ,["CAD - WILLSON INTERNATIONAL 1-800-871-1918 cdnpars@willsonintl.com",
              "CAD - WILLSON INTERNATIONAL 1-800-871-1918 cdnpars@willsonintl.com"]]																 ,
        required=False)

    so = fields.Text(
        string="SO#",
        required=False)

    term = fields.Char(
        string='Term',
        required=False)


class PurchaseOrderLineInherit(models.Model):
    _inherit = 'purchase.order.line'

    bill_count = fields.Integer(
        string='Bill Count',
        required=False, related="order_id.invoice_count")

    purchase_qty_ordered = fields.Float(
        string='Qty Ordered Po',
        required=False,readonly=True, related="product_qty")

    _field_Vhfzt = fields.Integer(
        string='New Related Field',
        required=False,readonly=True, related="order_id.picking_count")

    qty_ordered = fields.Float(
        string='Qty Ordered',
        required=False,readonly=True)

    stellar_status_po = fields.Char(
        string='Stellar_status_po',
        required=False,readonly=True, related="order_id.purchase_stellar_status")

