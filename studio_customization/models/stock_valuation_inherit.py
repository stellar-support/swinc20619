from odoo import models, fields, api


class StockValuationInherit(models.Model):
    _inherit = 'stock.valuation.layer'

    qty_at_date_1 = fields.Float(
        string='Quantity Stock + RMA',
        required=False, readonly=True, copy=True)

    stock_value = fields.Float(
        string='Cost Amount',
        required=False, readonly=True, copy=True)

    lst_price = fields.Float(
        'Public Price')

    unit_price = fields.Monetary(
        tring='Price',
        required=False, readonly=True, copy=True)
