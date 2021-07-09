from odoo import models, fields, api

class ProductInheritProduct(models.Model):
    _inherit = 'product.product'

    qty_at_date_1 = fields.Float(
        string='Quantity Stock + RMA',
        required=False,readonly=True,copy=True)

    stock_value_1 = fields.Float(
        string='Cost Amount',
        required=False,readonly=True,copy=True)

    field_EI5S4 = fields.Char(
        string='Vendor',
        required=False,readonly=True, related="product_tmpl_id.field_EI5S4")

    field_OX9au = fields.Char(
        string='New Related Field',
        required=False,readonly=True, related="product_tmpl_id.field_OX9au")

    field_cghBZ = fields.One2many(
        comodel_name='sale.report',
        inverse_name='product_id',
        string=' Sales price list by item',
        required=False, related="product_tmpl_id.field_cghBZ")

    field_rghuK = fields.One2many('purchase.report', 'product_id', string="Lista de PO", related="product_tmpl_id.field_rghuK")

    incoming_items = fields.Float(
        string='Qty Incoming',
        required=False, related="product_tmpl_id.incoming_items")

    pricelist_name = fields.Many2one(
        comodel_name='product.pricelist',
        string='Pricelist Name',
        required=False)

    qty_incoming = fields.Float(
        string='Qty Incoming',
        required=False, related="product_tmpl_id.qty_incoming")

    qty_outgoing = fields.Float(
        string='Qty Outgoing',
        required=False, related="product_tmpl_id.qty_outgoing")

    qty_sold = fields.Float(
        string='Qty sold',
        required=False, related="product_tmpl_id.qty_sold")

    vendor_name = fields.Char(
        string='Vendor Name',
        required=False,readonly=True, related="product_tmpl_id.seller_ids.display_name")

    unit_price = fields.Monetary(
        string='Price',
        required=False,readonly=True,copy=True)

    # @api.depends('lst_price')
    # def _compute_unit_price_(self):
    #     for record in self:
    #         record['unit_price'] = record.lst_price * record.qty_in_rent


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    field_EI5S4 = fields.Char(
        string='Vendor',
        required=False,readonly=True, related="product_variant_id.vendor_name")

    field_OX9au = fields.Char(
        string='New Related Field',
        required=False,readonly=True, related="product_variant_id.create_uid.display_name")

    field_cghBZ = fields.One2many(
        comodel_name='sale.report',
        inverse_name='product_id',
        string='Sales price list by item',
        required=False)

    field_rghuK = fields.One2many('purchase.report', 'product_id')

    incoming_items = fields.Float(
        string='Qty Incoming',
        required=False, related="product_variant_id.incoming_qty")

    pricelist_name = fields.Many2one(
        comodel_name='product.pricelist',
        string='Pricelist Name',
        required=False)

    qty_incoming = fields.Float(
        string='Qty Incoming',
        required=False, related="product_variant_id.incoming_qty")

    qty_outgoing = fields.Float(
        string='Qty Outgoing',
        required=False, related="product_variant_id.outgoing_qty")

    qty_sold = fields.Float(
        string='Qty sold',
        required=False, related="product_variant_id.sales_count")

    product_variant_id = fields.Many2one(search='_search_product_variant')

    def _search_product_variant(self, operator, value):
        """ Enable search on the field product_variant_id."""
        templates = self.env['product.product'].search([
            ('id', operator, value)
        ]).mapped('product_tmpl_id')

        return [('id', 'in', templates.ids)]