# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.exceptions import ValidationError
from odoo.tests import common
from .common import StellarTransactionCase


@common.tagged('post_install', '-at_install')
class TestPaymentStellar(StellarTransactionCase):

    def setUp(self):
        super().setUp()
        self.payment_transaction = self.env['payment.transaction'].sudo()
        self.sale_order = self.env['sale.order']

        self.product_4 = self.env.ref('product.product_product_4')
        self.partner_4 = self.env.ref('base.res_partner_4')
        self.normal_delivery = self.env.ref('delivery.normal_delivery_carrier')

        # Create journal
        self.create_missing_journal_for_acquirers()

        # Create sales order with Normal Delivery Charges
        self.sale_order_1 = self.sale_order.create({
            'partner_id': self.partner_4.id,
            'order_line': [(0, 0, {
                'name': 'PC Assamble + 2GB RAM',
                'product_id': self.product_4.id,
                'product_uom_qty': 1,
                'price_unit': 750.00,
            })],
            'carrier_id': self.normal_delivery.id
        })

    def test_01_payment_transaction(self):
        # In order to test a payment_transaction with stellar

        self.normal_delivery.pickup_warehouse = True
        sale_order = self.sale_order_1

        # I add delivery cost in Sales order
        sale_order.get_delivery_price()
        sale_order.set_delivery_line()

        # Create TX
        transaction = sale_order._create_payment_transaction({
            'acquirer_id': self.payment_stellar.id
        })

        post = {
            'return_url': self.payment_stellar.stellar_get_form_action_url(),
            'reference': transaction.reference,
            'amount': sale_order.amount_total,
            'currency': sale_order.pricelist_id.currency_id.name
        }

        # Check pre-states
        self.assertEqual(transaction.state, 'draft', "Wrong tx pre-state")
        self.assertEqual(sale_order.state, 'draft', "Wrong order pre-state")

        # Validate tx
        self.payment_transaction.form_feedback(post, 'stellar')

        # Check states
        self.assertEqual(transaction.state, 'pending', "Wrong tx state")
        self.assertEqual(sale_order.state, 'sent', "Wrong order state")

    def test_02_no_reference_transaction(self):
        # In order to test a transaction found
        reference = 'STELLAR-REFERENCE'
        with self.assertRaises(ValidationError):
            self.payment_transaction._stellar_form_get_tx_from_data({
                'reference': reference,
            })

    def test_03_no_invalid_parameters(self):
        # In order to test invalid parameters in tx
        sale_order = self.sale_order_1

        # Create TX
        transaction = sale_order._create_payment_transaction({
            'acquirer_id': self.payment_stellar.id
        })

        # Validate amount
        invalid_amount = {
            'amount': 800,
            'currency': sale_order.pricelist_id.currency_id.name
        }
        invalid_parameters = transaction._stellar_form_get_invalid_parameters(invalid_amount)
        self.assertTrue(invalid_parameters)

        # Validate currency
        invalid_currency = {
            'amount': sale_order.amount_total,
            'currency': 'Stellar',
        }
        invalid_parameters = transaction._stellar_form_get_invalid_parameters(invalid_currency)
        self.assertTrue(invalid_parameters)

        # Correct information
        tx_data = {
            'reference': transaction.reference,
            'amount': sale_order.amount_total,
            'currency': sale_order.pricelist_id.currency_id.name
        }
        invalid_parameters = transaction._stellar_form_get_invalid_parameters(tx_data)
        self.assertFalse(invalid_parameters)
