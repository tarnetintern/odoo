from odoo import models, fields, api

class SuruBolunmus(models.Model):
    _name = 'suru.bolunmus'
    _description = 'Suru Bolunmus'

    name = fields.Char("Bolunmus Harita Adı")
    tarih = fields.Datetime('Yükleme Tarihi', default=fields.Datetime.now)
    dosyaSahibi = fields.Char("Dosya Sahibi")
    bolunmusHaritaSayisi = fields.Integer("Bolunme Sayısı")
    dosyaYukleme1 = fields.Binary("Dosya1", attachment=True)
    dosyaYukleme2 = fields.Binary("Dosya2", attachment=True)
    dosyaYukleme3 = fields.Binary("Dosya3", attachment=True)
    dosyaYukleme4 = fields.Binary("Dosya4", attachment=True)
    dosyaYukleme5 = fields.Binary("Dosya5", attachment=True)
    dosyaYukleme6 = fields.Binary("Dosya6", attachment=True)
    dosyaYukleme7 = fields.Binary("Dosya7", attachment=True)
    
