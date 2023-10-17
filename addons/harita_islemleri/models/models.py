from odoo import models, fields, api

class harita_islemleri(models.Model):
    _name = 'harita_islemleri.harita_islemleri'
    _description = 'harita_islemleri.harita_islemleri'

    _populate_dependencies = ['res.users']

    name = fields.Char("Harita Adı")
    description = fields.Text("Açıklama")
    sehir = fields.Many2one('sehir',string= 'Şehir')
    harita_adres = fields.Many2one('harita.adres',string= 'Açık Adres')
    pilot_id = fields.Many2many('res.users',string='Pilot')
