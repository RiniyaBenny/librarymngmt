# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': """
        Library Management""",

    'description': """
        Manage a Library: customers, books, etc.... 
        """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        #'data/librarymngmt_data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/librarymngmt.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
