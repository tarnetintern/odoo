# -*- coding: utf-8 -*-
{
    'name': "Görev İlaçları",
    'summary': """
        Görevlerde kullanılabilecek olan ilaçların bilgisinin tutulması ve daha sonra görev modülüne entegre edilmesi amacıyla geliştirilmiştir.""",
    'description': """
        Görevlerde kullanılabilecek olan ilaçların bilgisinin tutulması ve daha sonra görev modülüne entegre edilmesi amacıyla geliştirilmiştir.
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
    'sequence':-98,
}
