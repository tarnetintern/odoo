from odoo import models, fields, api

class GorevAdres(models.Model):
    _name = 'gorev.adres'
    _description = 'gorev.adres'
    _rec_name = 'adres_name'
    
    adres_name = fields.Char("Adres Başlığı")
    il = fields.Char("İl")
    ilce = fields.Char("İlçe")
    mahalle = fields.Char("Mahalle")
    adaNo = fields.Integer("Ada No")
    parselNo = fields.Integer("Parsel No")

    #task_ids = fields.Many2one('gorev_takip.gorev_takip',string ='Görev(İsteğe Bağlı) ',required=False)