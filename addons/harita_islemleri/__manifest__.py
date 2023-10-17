# -*- coding: utf-8 -*-
{
    'name': "Harita Islemleri",
    'summary': """Pilotlarin mevcut olan haritalari sisteme yuklemesi 
                ve sistemden kumandaya aktarmasi icin yapilmistir.""",
    'description': """
        Pilotlarin mevcut olan haritalari sisteme yuklemesi 
         ve sistemden kumandaya aktarmasi icin yapilmistir.
    """,
    'author': "Tarik Sariyildiz",
    'category': 'business',
    'version': '1.0',
    'sequence':-105,
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
