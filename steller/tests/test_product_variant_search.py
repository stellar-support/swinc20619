# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import common


@common.tagged('post_install', '-at_install')
class TestVariantSearch(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.template = self.env['product.template']
        self.product_4 = self.env.ref('product.product_product_4')

    def test_01_equal_search(self):
        # In order to test search with operator(=)
        product_variant_id = self.template.search([('product_variant_id', '=', self.product_4.id)])

        # the address must be the same
        self.assertEqual(product_variant_id, self.product_4.product_tmpl_id, "Search with (=) fails")

    def test_02_not_equal_search(self):
        # In order to test search with operator(!=)
        product_variant_id = self.template.search([('product_variant_id', '!=', self.product_4.id)])

        # the address must be the same
        self.assertNotEqual(product_variant_id, self.product_4.product_tmpl_id, "Search with (!=) fails")

    def test_03_in_search(self):
        # In order to test search with operator(in)
        product_variant_id = self.template.search([('product_variant_id', 'in', self.product_4.ids)])

        # the address must be the same
        self.assertEqual(product_variant_id, self.product_4.product_tmpl_id, "Search with (in) fails")

    def test_04_not_in_search(self):
        # In order to test search with operator(not in)
        product_variant_id = self.template.search([('product_variant_id', 'not in', self.product_4.ids)])

        # the address must be the same
        self.assertNotEqual(product_variant_id, self.product_4.product_tmpl_id, "Search with (not in) fails")
