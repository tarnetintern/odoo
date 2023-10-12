# -*- coding: utf-8 -*-
{
    'name': "Görev Takip",
    'summary': "Operasyon birimlerinin görevlerini takip edip analiz etmek amacıyla yapılmıştır.",
    'description': """
        Pilotların göreve gittiği adres bilgileri, görevde kullancağı ilaç bilgileri,görevin durumu ve görevde hangi pilotun aktif olduğu bilgilerinin kolayca tutulması ve analiz edilmesi için geliştirilmiştir.
    """,
    'author': "Batuhan OKMEN",
    'category': 'business',
    'version': '1.0',
    'sequence':-100,
    'depends': ['base',"resource"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',   
    ],
    "application":True,
    "installable":True,
    "license":'LGPL-3'
}
