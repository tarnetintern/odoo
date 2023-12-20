# -*- coding: utf-8 -*-
{
    'name': "Görev Yükleme",
    'summary': """
        Var olan oluşturulmuş haritanın sisteme yüklenmesi.""",
    'description': """
        Haritaların sisteme hangi pilot tarafından ne zaman yüklendiği bilgilerini içerir.
    """,
    'author': "Batuhan OKMEN",
    'category': 'Business',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'sequence':-99,
    "application":True,
    "installable":True,
    "license":'LGPL-3',
}
