from odoo import models, fields, api

class ProductInheritProduct(models.Model):
    _inherit = 'product.product'

    qty_at_date_1 = fields.Float(
        string='Quantity Stock + RMA',
        required=False,readonly=True,copy=True)

    stock_value = fields.Float(
        string='Cost Amount',
        required=False,readonly=True,copy=True)

    field_EI5S4 = fields.Char(
        string='Vendor',
        required=False,readonly=True)

    field_OX9au = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    field_cghBZ = fields.One2many(
        comodel_name='sale.report',
        inverse_name='product_id',
        string=' Sales price list by item',
        required=False)

    field_rghuK = fields.One2many('purchase.report', 'product_id')

    incoming_items = fields.Float(
        string='Qty Incoming',
        required=False)

    pricelist_name = fields.Many2one(
        comodel_name='product.pricelist',
        string='Pricelist Name',
        required=False)

    qty_incoming = fields.Float(
        string='Qty Incoming',
        required=False)

    qty_outgoing = fields.Float(
        string='Qty Outgoing',
        required=False)

    qty_sold = fields.Float(
        string='Qty sold',
        required=False)

    vendor_name = fields.Char(
        string='Vendor Name',
        required=False,readonly=True)

    unit_price = fields.Monetary(
        tring='Price',
        required=False,readonly=True,copy=True)

    # @api.depends('lst_price')
    # def _compute_unit_price_(self):
    #     for record in self:
    #         record['unit_price'] = record.lst_price * record.qty_in_rent


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    field_EI5S4 = fields.Char(
        string='Vendor',
        required=False,readonly=True)

    field_OX9au = fields.Char(
        string='New Related Field',
        required=False,readonly=True)

    field_cghBZ = fields.One2many(
        comodel_name='sale.report',
        inverse_name='product_id',
        string='Sales price list by item',
        required=False)

    field_rghuK = fields.One2many('purchase.report', 'product_id')

    incoming_items = fields.Float(
        string='Qty Incoming',
        required=False)

    pricelist_name = fields.Many2one(
        comodel_name='product.pricelist',
        string='Pricelist Name',
        required=False)

    qty_incoming = fields.Float(
        string='Qty Incoming',
        required=False)

    qty_outgoing = fields.Float(
        string='Qty Outgoing',
        required=False,)

    qty_sold = fields.Float(
        string='Qty sold',
        required=False)


