from odoo import fields, models


class PaymentAcquirerCredit(models.Model):

    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('stellar', 'Stellar')], required=False,)

    def stellar_get_form_action_url(self):
        """ Returns the form action URL, for form-based acquirer implementations. """
        return '/payment/stellar/feedback'

    def _get_feature_support(self):
        """Get advanced feature support by provider."""
        res = super()._get_feature_support()
        res['authorize'].append('stellar')
        return res
