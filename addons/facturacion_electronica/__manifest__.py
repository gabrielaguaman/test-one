# -*- coding: utf-8 -*-
{
    'name': "Facturacion Electronica",

    'summary': """
        Integrar facturacion electronica con pos""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/book.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/report_book.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}