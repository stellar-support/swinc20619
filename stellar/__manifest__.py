# Copyright 2020 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Instance Creator for Stellar',
    'summary': '''
    Instance creator for stellar. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'LGPL-3',
    'category': 'Installer',
    'version': '12.0.1.0.0',
    'depends': [
        'account_batch_payment',
        'account_cancel',
        'account_check_printing',
        'account_payment',
        'account_reports_followup',
        'base_import_module',
        'base_vat',
        'board',
        'crm',
        'delivery',
        'l10n_ca',
        'sale_coupon',
        'sale_margin',
        'stock_barcode',
        'stock_dropshipping',
        'theme_bootswatch',
        'website_form_editor',
        'website_partner',
        'website_sale',
    ],
    'test': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_team.xml',
        'data/res_company.xml',
        'data/res_config_settings.xml',
        'report/report_dwjo_views.xml',
        'report/report_dwjo.xml',
        'report/report_dwjo_template.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
