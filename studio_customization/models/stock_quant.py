from odoo import models, fields, api

class StockQuantInherit(models.Model):
    _inherit = 'stock.quant'

    cost = fields.Float(string='Cost', related="product_tmpl_id.standard_price")
    cost_total = fields.Char(compute='_compute_field_name', string='Total Cost')
    
    @api.depends('cost')
    def _compute_cost_total(self):
        for record in self:
            record['cost_total'] = record.cost * record.quantity
    