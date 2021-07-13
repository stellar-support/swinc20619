# Copyright 2021 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests import common
from .common import StellarHttpCase


@common.tagged('post_install', '-at_install')
class TestPaymentStellarTour(StellarHttpCase):

    def setUp(self):
        super().setUp()
        # Create journal
        self.create_missing_journal_for_acquirers()

    def test_01_payment_transaction(self):
        """ In order to test a payment_transaction with stellar"""
        url = '/shop'
        tour = 'stellar_payment'
        self.phantom_js(
            url_path=url, code="odoo.__DEBUG__.services['web_tour.tour'].run('%s')" % tour,
            ready="odoo.__DEBUG__.services['web_tour.tour'].tours.%s.ready" % tour,
            login="admin")

        # Get the new order
        order = self.env['sale.order'].search([], limit=1, order='id DESC')
        tx = order.transaction_ids[:1]

        self.assertEqual(order.state, 'sent', "Wrong order state")

        self.assertEqual(tx.state, 'pending', "Wrong TX state")

        self.assertEqual(tx.acquirer_id, self.payment_stellar, "Wrong acquirer")
