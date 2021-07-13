# Copyright 2021 Vauxoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import HttpCase, TransactionCase
import psycopg2


class StellarCase:

    def setUp(self):
        super().setUp()
        self.payment_stellar = self.env.ref('stellar.payment_acquirer_stellar', False)
        self.journal_model = self.env['account.journal']

    def create_missing_journal_for_acquirers(self):
        """Create the journal for the new payment"""
        if not self.payment_stellar or self.payment_stellar.journal_id:
            return False

        try:
            with self.env.cr.savepoint():
                self.payment_stellar.journal_id = self.journal_model.create(
                    self.payment_stellar._prepare_account_journal_vals())
        except psycopg2.IntegrityError as e:
            if e.pgcode == psycopg2.errorcodes.UNIQUE_VIOLATION:
                self.payment_stellar.journal_id = self.journal_model.search(
                    self.payment_stellar._get_acquirer_journal_domain(), limit=1)


class StellarTransactionCase(StellarCase, TransactionCase):
    pass


class StellarHttpCase(StellarCase, HttpCase):
    pass
