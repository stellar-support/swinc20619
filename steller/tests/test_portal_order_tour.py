# Copyright 2021 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests import common


@common.tagged('post_install', '-at_install')
class TestPortalOrderTour(common.HttpCase):

    def test_01_portal_order(self):
        """In order to test the new order in /my/orders."""
        url = '/my/orders'
        tour = 'portal_order'
        self.phantom_js(
            url_path=url, code="odoo.__DEBUG__.services['web_tour.tour'].run('%s')" % tour,
            ready="odoo.__DEBUG__.services['web_tour.tour'].tours.%s.ready" % tour,
            login="admin")
