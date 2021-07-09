from odoo import models, fields, api


class StockPickingStage(models.Model):
    _name = 'stock.picking.stage'

    display_name = fields.Char(
        string='Display Name',
        required=False,readonly=True)

    name = fields.Char(
        string='Name',
        required=False)
