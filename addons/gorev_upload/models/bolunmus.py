from odoo import models, fields, api

class SuruBolunmus(models.Model):
    _name = 'suru.bolunmus'
    _description = 'Suru Bolunmus'

    name = fields.Char("Bolunmus Harita Adı")
    tarih = fields.Datetime('Yükleme Tarihi', default=fields.Datetime.now)
    dosyaSahibi = fields.Char("Dosya Sahibi")
    bolunmusHaritaSayisi = fields.Integer("Bolunme Sayısı")
    harita_ids = fields.One2many('suru.bolunmus.harita', 'bolunmus_id', string="Haritalar")

class SuruBolunmusHarita(models.Model):
    _name = 'suru.bolunmus.harita'
    _description = 'Suru Bolunmus Harita'
    name=fields.Char("Parca Harita Adı")
    dosyaSahibi = fields.Char("Parca Dosya Sahibi")
    tarih = fields.Datetime('Yükleme Tarihi', default=fields.Datetime.now)
    bolunmusHaritaSayisi = fields.Integer("Bolunme Sayısı")
    harita_ids = fields.One2many('suru.bolunmus.harita', 'bolunmus_id', string="Haritalar", readonly=True)
    bolunmus_id = fields.Many2one('suru.bolunmus.harita', string="Bölünmüş Harita")
    harita_dosyasi = fields.Binary("Dosya", attachment=True)