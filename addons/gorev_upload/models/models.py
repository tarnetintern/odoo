#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timezone


class gorev_upload(models.Model):
    _name = 'gorev_upload.gorev_upload'
    _description = 'gorev_upload.gorev_upload'
    _defaults = {
    'date_action': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
    }

    name = fields.Char("Harita adı")
    tarih = fields.Datetime('Date current action', default=fields.Datetime.now, required=False, readonly=False, select=True)
    #tarih = fields.datetime("Yükleme Tarihi", default=lambda self: fields.Datetime.now())
    #tarih = fields.Char("tarih")
    dosyaYukleme = fields.Binary("Dosya", attachment=True)  # Dosyayı saklamak için Binary alan
    dosyaSahibi = fields.Char("Dosya Sahibi")
    


