odoo.define("stellar.portal_order_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    // In order to test the new order in /my/orders
    tour.register("portal_order", {
        test: true,
        url: '/my/orders',
        wait_for: base.ready(),
    },
    [
        {
            content: "Show options",
            trigger: "#portal_searchbar_sortby",
            run: 'click',
        },
        {
            content: "Select order state",
            trigger: "#o_portal_navbar_content a[href*='orders?sortby=stage']",
            run: 'click',
        },
        {
            content: "Select order field",
            trigger: ".o_portal_my_doc_table th.order_state",
            run: 'click',
        },
    ]);
});
