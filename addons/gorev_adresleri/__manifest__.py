# -*- coding: utf-8 -*-
{
    'name': "Görev Adresleri",
    'summary': """
        Görev yapılan veya yapılacak adreslerin kaydedilmesi ve daha sonra görev takip modülüne entegre edilmesi gerekmektedir.""",
    'description': """
        İlaçlama yapılacak adreslerin bilgisinin tutulması ve daha sonrasında görevlere adres olarak eklenmesi için adresleri ayrı modül üzerinde tutmak amacıyla yazılmıştır.
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
