import logging
import pprint

from odoo import http, _
from odoo.exceptions import ValidationError
from odoo.http import request
from odoo.addons.sale.controllers.portal import CustomerPortal

_logger = logging.getLogger(__name__)


class PaymentController(http.Controller):

    @http.route(['/payment/stellar/feedback'], type='http', auth='user', website=True)
    def stellar_form_feedback(self, **post):
        """Get and Validate the payment transaction"""
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))
        response = request.env['payment.transaction'].sudo().form_feedback(post, 'stellar')
        if response:
            return request.redirect('/payment/process')
        return request.redirect('/shop/payment')

    @http.route(['/payment/stellar/check_payment'], type='json', auth="user", website=True)
    def check_payment(self, acquirer_id, **kwargs):
        """ Json method that validate orders, before sending to process.

        :param acquirer_id: id of a payment.acquirer record. If not set the
                            user is redirected to the checkout page
        :type acquirer_id:  int
        """
        # Ensure a payment acquirer is selected
        if not acquirer_id:
            return False

        try:
            acquirer_id = int(acquirer_id)
        except ValueError:
            return False

        # Retrieve the sale order
        order = request.website.sale_get_order()

        # Ensure there is something to proceed
        if not order or not order.order_line:
            return False

        # Validate the order amount
        if order.amount_total <= 0:
            raise ValidationError(_('The order amount must be higher than 0'))

        return True

    @http.route(['/payment/stellar/save_note'], type='json', auth="user", website=True)
    def save_note(self, partner_note=None):
        """ Saves the order note entered by the customer.

        :param partner_note: order note
        :type partner_note: str

        """
        # Ensure a payment acquirer is selected
        order = request.website.sale_get_order()
        if partner_note and order:
            order.write({'partner_note': partner_note})

        return True


class CustomerPortalStellar(CustomerPortal):

    @http.route()
    def portal_my_orders(self, page=1, date_begin=None, date_end=None, sortby='stage', **kw):
        """Replace stage order by state."""
        res = super().portal_my_orders(page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw)
        if not res.qcontext.get('searchbar_sortings'):
            return res

        # Add statur order
        res.qcontext['searchbar_sortings']['stage'].update({
            'label': _('State'),
        })

        return res

    @http.route()
    def account(self, redirect=None, **post):
        """Disable editing of the billing address."""
        return request.redirect('/my')
