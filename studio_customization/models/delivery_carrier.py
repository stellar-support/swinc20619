from odoo import fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    pickup_warehouse = fields.Boolean(
        'Pickup in Warehouse', help="If the package will be Pickup in a warehouse", default=False)
    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Warehouse', help="If the package will be Pickup in a warehouse")
