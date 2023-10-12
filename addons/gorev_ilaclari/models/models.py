# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gorev_ilaclari(models.Model):
    _name = 'gorev_ilaclari.gorev_ilaclari'
    _description = 'gorev_ilaclari.gorev_ilaclari'

    title = fields.Char("İlaç Başlığı")
    usesofMedicine = fields.Char("İlacın Kullanım Alanları")

