from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_variant_id = fields.Many2one(search='_search_product_variant')

    def _search_product_variant(self, operator, value):
        """ Enable search on the field product_variant_id."""
        templates = self.env['product.product'].search([
            ('id', operator, value)
        ]).mapped('product_tmpl_id')

        return [('id', 'in', templates.ids)]
