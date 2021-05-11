odoo.define('stellar.saleOrder', function (require) {
    "use strict";

    // var emojis = require('mail.emojis');
    // var MentionManager = require('mail.composer.MentionManager');
    // var DocumentViewer = require('mail.DocumentViewer');
    // var mailUtils = require('mail.utils');

    // var config = require('web.config');
    // var core = require('web.core');
    // var data = require('web.data');
    // var dom = require('web.dom');
    // var session = require('web.session');
    var Widget = require('web.Widget');

    // var QWeb = core.qweb;
    // var _t = core._t;

    // var BasicComposer = require('mail.composer.Basic')

    var StellarSaleOrder = Widget.extend({
        template: 'sale_order_form',
        events: {
            'click .send_confirmation_email': '_sendConfirmationEmail',
        },


        _sendConfirmationEmail: function () {
            console.log('YOU CLICKED HERE!');

            // var self = this;
            // return self.rpc('/sale_order_confirmation_mail');
        },

    });

    {
        return StellarSaleOrder;
    };

});