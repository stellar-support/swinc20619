odoo.define('studio_customization.payment.processing', (require) => {
    'use strict';

    var publicWidget = require('web.public.widget');
    var PaymentProcessing = require('payment.processing');

        publicWidget.registry.PaymentProcessing.include({
        start: function() {
            this._super.apply(this, arguments);
        },
        processPolledData: function (transactions) {
            if (transactions.length > 0 && transactions[0].acquirer_provider == 'studio_customization') {
                window.location = transactions[0].return_url;
                return;
            }
            this._super.apply(this, arguments);
        },
    });
});
