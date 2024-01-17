from odoo import models, fields, api

class gorev_upload_bolunmus(models.Model):
    _name = 'gorev_upload_bolunmus.gorev_upload_bolunmus'
    _description = 'gorev_upload_bolunmus.gorev_upload_bolunmus'
    
    name = fields.Char("Bolunmus Harita Adı")
    tarih = fields.Datetime('Yükleme Tarihi', default=fields.Datetime.now, required=False, readonly=False, select=True)
    dosyaSahibi = fields.Char("Dosya Sahibi")
    bolunmusHaritaSayisi=fields.Integer("Bolunme Sayısı")
    #pilot_task_ids = fields.Many2one('gorev_takip.gorev_takip',string ='Görev(İsteğe Bağlı) ',required=False)