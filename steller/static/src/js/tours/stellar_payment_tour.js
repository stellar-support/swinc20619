odoo.define("stellar.stellar_payment_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    tour.register("stellar_payment", {
        test: true,
        url: '/shop',
        wait_for: base.ready(),
    },
    [
        {
            content: "Select a product",
            trigger: "#products_grid td.oe_product section h6 a:contains('Warranty')",
            run: 'click',
        },
        {
            content: "Add product",
            trigger: "#add_to_cart",
            run: 'click',
        },
        {
            content: "Checkout",
            trigger: ".oe_cart .row .btn-primary",
            run: 'click',
        },
        {
            content: "Select stellar payment",
            trigger: "input[data-provider='stellar']",
            run: 'click',
        },
        {
            content: "Pay",
            trigger: "#o_payment_form_pay",
            run: 'click',
        },
        {
            content: "Success Confirmation",
            trigger: ".card-header.bg-info",
            run: 'click',
        },
        
    ]);
});
