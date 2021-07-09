from odoo import api, models, _
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare

import logging
import pprint

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):

    _inherit = 'payment.transaction'

    @api.model
    def _stellar_form_get_tx_from_data(self, data):
        """ Given a data dict coming from stellar payment, verify it and find the related transaction record."""
        reference = data.get('reference')
        tx = self.search([('reference', '=', reference)])

        if not tx or len(tx) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return tx

    def _stellar_form_get_invalid_parameters(self, data):
        """Get  invalid parameters."""
        invalid_parameters = []

        # verifies that the amount to pay is equal to the total of the order
        if float_compare(float(data.get('amount') or '0.0'), self.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % self.amount))
        # verifies that the currency to pay is equal to the order
        if data.get('currency') != self.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), self.currency_id.name))

        return invalid_parameters

    def _stellar_form_validate(self, data):
        """Authorize the transaction before processing it."""
        _logger.info('Validated transfer payment for tx %s: set as pending', self.reference)
        try:
            self._set_transaction_pending()
        except Exception as e:
            self._set_transaction_error(str(e))

        return True

    def _set_transaction_pending(self):
        # Override of '_set_transaction_pending' in the 'payment' module
        # to add stellar actions.
        response = super()._set_transaction_pending()

        for record in self.filtered(lambda t: t.acquirer_id.provider == 'stellar'):
            # Get reference
            for so in record.sale_order_ids:
                so.reference = record._compute_sale_order_reference(so)
                # Update address and send emails to the group online
                so.action_confirm_stellar()
        return response
