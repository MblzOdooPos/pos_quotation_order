{
    'name': "Reservas desde POS y Website",
    'version': '14.0.1.0.0',
    'summary': """Create & Process Quotation from POS and Website""",
    'description': """This module allows to create and process quotation orders from POS and Website""",
    'author': "Felipe Angulo",
    'company': "Pudutechnology",
    'website': "http://www.pudutechnology.cl",
    'category': 'Pudutechnology',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/quotation_templates.xml',
        'views/web_templates.xml',
        'views/pos_quotation.xml',
    ],
    'qweb': [
        'static/src/xml/Chrome.xml',
        'static/src/xml/Buttons.xml',
        'static/src/xml/Popups.xml',
        'static/src/xml/Receipts.xml',
        'static/src/xml/Screens.xml',
        ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': True,
}
