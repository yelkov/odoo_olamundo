# -*- coding: utf-8 -*-
{
    'name': "odoo_olamundo",

    'summary': "Proxecto inicial de Ola Mundo",

    'description': """
Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo!Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo! Benvido ao proxecto Ola mundo!
    """,

    'author': "a23yelkovq",
    'website': "https://www.edu.xunta.gal/centros/iesteis",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'views/olamundo.xml',
        'views/menu.xml',
        'views/templates.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

