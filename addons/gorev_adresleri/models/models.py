#-*- coding: utf-8 -*-

from odoo import models, fields, api


class gorev_adresleri(models.Model):
    _name = 'gorev_adresleri.gorev_adresleri'
    _description = 'gorev_adresleri.gorev_adresleri'

    name = fields.Char("Adres Başlığı")
    il = fields.Char("İl")
    ilce = fields.Char("İlçe")
    mahalle = fields.Char("Mahalle")
    adaNo = fields.Integer("Ada No")
    parselNo = fields.Integer("Parsel No")

