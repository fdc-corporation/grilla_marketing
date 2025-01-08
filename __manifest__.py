# -*- coding: utf-8 -*-
{
    'name': "grillas_marketing",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo para la integracion de funcionalidades en funcion al area de Marketing
        Panel de agenda para grillas de de Redes Sociales
    """,

    'author': "Yostin Palacios",
    'website': "https//fdc-corporation.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', "calendar"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/marca_view.xml',
        'views/plataformas_view.xml',
        'views/responsables_view.xml',
        'views/formatos_view.xml',
        'views/proyctos_view.xml',
        'views/evento-proyecto.xml',
        'views/code/ir.cronp.xml'
    ],
}









