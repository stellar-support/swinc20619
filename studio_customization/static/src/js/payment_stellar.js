odoo.define('stellar.payment_stellar', (require) => {
    'use strict';

    const PaymentForm = require('payment.payment_form');
    const ajax = require('web.ajax');
    const { _t } = require('web.core');

    PaymentForm.include({
        events: _.extend(PaymentForm.prototype.events, {
            'click input[data-acquirer-id]': 'OnStellarPayment',
            'blur #partner_note': 'saveNotes',
        }),
        start () {
            this._super();
            this.OnStellarPayment({ currentTarget: this.$('.card input[data-provider]:checked').eq(0) });
        },
        OnStellarPayment (ev) {
            this._OnStellarPayment = $(ev.currentTarget).data('provider') === 'stellar';
        },
        payEvent (ev) {
            ev.preventDefault();
            this.parentPayEvent = this._super.bind(this, ...arguments);
            this.button = ev.target;
            this.saveNotes();
        },
        saveNotes (ev) {
            // If the initiador is onBlur(False) or payEvent(True)
            var payEventAfter = !ev;
            var self = this;
            // Save order note
            return ajax.rpc('/payment/stellar/save_note/', {
                'partner_note': this.$('#partner_note').val(),
            }).then(function () {
                if (payEventAfter) {
                    self.payEventAfter();
                }
            });

        },
        payEventAfter () {

            if (!this._OnStellarPayment) {
                this.parentPayEvent();
                return;
            }

            var checked_radio = this.$('input[type="radio"]:checked');
            var self = this;
            var button = this.button;
            var acquirer_id = this.getAcquirerIdFromRadio(checked_radio[0]);
            this.disableButton(button);

            // First we check that the user has selected a payment method
            ajax.jsonRpc('/payment/stellar/check_payment/', 'call', {
                'acquirer_id': parseInt(acquirer_id),
                'order_id': self.options.orderId,
                'access_token': self.options.accessToken,
            }).then(function (result) {
                if (result) {
                    // If the server sent us a valid result, we we continue with the normal flow
                    $(button).find('span.o_loader').remove();
                    self.parentPayEvent();
                    return;
                }
                
                self.displayError(
                    _t('Server Error'),
                    _t("We are not able to redirect you to the payment form.")
                );
                self.enableButton(button);
            }).fail(function (error, event) {
                self.displayError(
                    _t('Payment Error'),
                    error.data.message
                );
                self.enableButton(button);
            });
        },
    });
});
