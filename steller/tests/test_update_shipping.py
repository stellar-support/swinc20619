# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import common


@common.tagged('post_install', '-at_install')
class TestUpdateShipping(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.sale_order = self.env['sale.order']

        self.product_4 = self.env.ref('product.product_product_4')
        self.partner_4 = self.env.ref('base.res_partner_4')
        self.free_delivery = self.env.ref('delivery.free_delivery_carrier')
        self.normal_delivery = self.env.ref('delivery.normal_delivery_carrier')
        self.pickup_delivery = self.env.ref('stellar.pickup_delivery')

    def test_01_no_update_Shipping(self):
        # In order to test a delivery without pickup_warehouse
        # Create sales order with Normal Delivery Charges
        self.sale_order = self.sale_order.create({
            'partner_id': self.partner_4.id,
            'order_line': [(0, 0, {
                'name': 'PC Assamble + 2GB RAM',
                'product_id': self.product_4.id,
                'product_uom_qty': 1,
                'price_unit': 750.00,
            })],
            'carrier_id': self.free_delivery.id
        })

        # I add delivery cost in Sales order
        self.sale_order.get_delivery_price()
        self.sale_order.set_delivery_line()

        # I confirm the sales order
        self.sale_order.action_confirm_stellar()

        # the address must be the same
        self.assertEqual(self.sale_order.partner_shipping_id, self.partner_4, "The address changed")

    def test_02_no_update_Shipping(self):
        # In order to test a delivery with pickup_warehouse but without warehouse
        # Create sales order with Normal Delivery Charges

        self.normal_delivery.pickup_warehouse = True
        self.sale_order = self.sale_order.create({
            'partner_id': self.partner_4.id,
            'order_line': [(0, 0, {
                'name': 'PC Assamble + 2GB RAM',
                'product_id': self.product_4.id,
                'product_uom_qty': 1,
                'price_unit': 750.00,
            })],
            'carrier_id': self.normal_delivery.id
        })

        # I add delivery cost in Sales order
        self.sale_order.get_delivery_price()
        self.sale_order.set_delivery_line()

        # I confirm the sales order
        self.sale_order.action_confirm_stellar()

        # the address must be the same
        self.assertEqual(self.sale_order.partner_shipping_id, self.partner_4, "The address changed")

    def test_03_update_Shipping(self):
        # In order to test a delivery with pickup_warehouse and without warehouse
        # Create sales order with Normal Delivery Charges

        self.sale_order = self.sale_order.create({
            'partner_id': self.partner_4.id,
            'order_line': [(0, 0, {
                'name': 'PC Assamble + 2GB RAM',
                'product_id': self.product_4.id,
                'product_uom_qty': 1,
                'price_unit': 750.00,
            })],
            'carrier_id': self.pickup_delivery.id
        })

        # I add delivery cost in Sales order
        self.sale_order.get_delivery_price()
        self.sale_order.set_delivery_line()

        # I confirm the sales order
        self.sale_order.action_confirm_stellar()

        # the address must not be the same
        self.assertNotEqual(self.sale_order.partner_shipping_id, self.partner_4, "The not address changed")
