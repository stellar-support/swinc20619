from odoo.tests import tagged
from odoo.addons.sale.tests.test_sale_common import TestCommonSaleNoChart


@tagged('sale_order')
class TestSaleOrder(TestCommonSaleNoChart):

    def test_01_send_sale_order_confirmation_email(self):
        salesteam = self.env['crm.team'].search([]).filtered(lambda t: t.name == 'Online')
        sales_user = self.env['res.users'].search([], limit=1)
        sales_user.update({'email': 'test@test.com', 'subscribed_to_confirmation_email': True, })
        salesteam.member_ids = sales_user
        partner = self.env['res.partner'].search([], limit=1)
        website = self.env['website'].search([], limit=1)
        sale_order = self.env['sale.order'].create({'partner_id': partner.id, 'website_id': website.id, })
        sale_order.action_confirm_stellar()
        mail = self.env['mail.message'].search([('record_name', '=', sale_order.name)], limit=1)
        self.assertTrue(mail)
