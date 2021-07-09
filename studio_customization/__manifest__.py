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
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','website_sale','stock','documents_account','product','stock_account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
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
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
