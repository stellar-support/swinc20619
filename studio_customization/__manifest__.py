# -*- coding: utf-8 -*-
{
    'name': "studio_customization",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','website_sale','stock','documents_account','product','stock_account', 'purchase','delivery','website_sale_delivery'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/res_company.xml',
        'data/delivery.xml',
        'data/ir_attachment.xml',
        'data/ir_cron.xml',
        'data/mail_template.xml',
        'data/crm_team.xml',
        'data/res_company.xml',
        'data/website.xml',
        'views/assets.xml',
        'views/account_move_inherit.xml',
        'views/res_partner_inherit.xml',
        'views/purchase_order_inherit.xml',
        'views/sale_order_inherit.xml',
        'views/product_inherit.xml',
        'views/stock_valuation_inherit.xml',
        'views/stock_production_lot_inherit.xml',
        'views/stock_move_line_inherit.xml',
        'views/stock_picking_inherit.xml',
        'views/stock_picking_stage.xml',
        'views/templates.xml',
        'views/bank_statement_view.xml',
        'views/delivery_views.xml',
        'views/res_users_views.xml',
        'report/report_dwjo_views.xml',
        'views/template/website_sale_templates.xml',
        'views/template/payment_templates.xml',
        'views/template/portal_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
