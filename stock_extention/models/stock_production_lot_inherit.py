from odoo import models, fields, api

class CrmLeadInherit(models.Model):
    _inherit = 'stock.production.lot'

    sales_order = fields.Char(
        string='Sale Order',
        required=False, readonly=True)
