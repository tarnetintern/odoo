# -*- coding: utf-8 -*-
{
    'name': "Batarya Takip",
    'summary': """
        Bataryaların kalan ömrünü takip etmek amacıyla geliştirilmiştir. İlerleyen süreçte cycle değeri bataryanın içindeki parametre ile güncellenebilir.""",
    'description': """
        Bataryaların kalan ömrünü takip etmek amacıyla geliştirilmiştir. İlerleyen süreçte cycle değeri bataryanın içindeki parametre ile güncellenebilir.
    """,
    'author': "Batuhan OKMEN",
    'category': 'business',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    "application":True,
    "installable":True,
    "license":'LGPL-3',
    "sequence":-97,
}
