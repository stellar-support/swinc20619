# Copyright 2021 Stellar Whlesale Inc
{
    'name': 'Instance Creator for Stellar',
    'summary': '''
    Instance creator for stellar. This is the app.
    ''',
    'author': 'Alfredo',
    'website': 'stellar.ca',
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
        'data/res_company.xml',
        'report/report_dwjo_views.xml',
        'report/report_dwjo.xml',
        'report/report_dwjo_template.xml',
        'views/bitacora.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
