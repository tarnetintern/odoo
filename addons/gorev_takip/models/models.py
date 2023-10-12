from odoo import models, fields, api


class gorev_takip(models.Model):
    _name = 'gorev_takip.gorev_takip'
    _description = 'gorev_takip.gorev_takip'

    _populate_dependencies = ['res.users']

    name = fields.Char("Görevin Başlığı")
    description = fields.Text("Görevin Açıklaması")
    isDone = fields.Selection([('yapiliyor','Yapılıyor'),('yapilmadi','Yapılmadı'),('yapildi','Yapıldı'),('iptal','İptal edildi')],string='Yapılma Durumu',default='yapiliyor')
    deneme = fields.Selection([('yapiliyor','Yapılıyor')],string='Personel',default='yapiliyor')
    donumBasinaUcret = fields.Integer("Dönüm başına ücret")
    adres_id = fields.Many2one('gorev.adres',string= 'Görevin Adresi')
    pilot_id = fields.Many2many('res.users',string='Görevdeki Pilotlar')#hr.employee#task.pilot
    medicine_id = fields.Many2many('task.medicine',string='Görevdeki İlaçlar')
    
    
    # address_id = fields.One2many('gorev.adres','task_ids',string='Görevin Adresi')
    # medicine_id = fields.One2many('task.medicine','medicine_task_ids',string='Görevde Kullanılan İlaçlar')
    # pilot_id = fields.One2many('task.pilot','pilot_task_ids',string='Görev Alan Pilotlar')





    