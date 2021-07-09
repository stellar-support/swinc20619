odoo.define('stellar.payment.processing', (require) => {
    'use strict';

    const PaymentProcessing = require('payment.processing');

    PaymentProcessing.include({
        processPolledData: function (transactions) {
            if (transactions.length > 0 && transactions[0].acquirer_provider == 'stellar') {
                window.location = transactions[0].return_url;
                return;
            }
            this._super.apply(this, arguments);
        },
    });
});
