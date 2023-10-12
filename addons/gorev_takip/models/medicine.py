from odoo import models, fields, api

class TaskMedicine(models.Model):
    _name = 'task.medicine'
    _description = 'task.medicine'
    
    name = fields.Char("İlaç Başlığı")
    usesofMedicine = fields.Char("İlacın Kullanım Alanları")

    #medicine_task_ids = fields.Many2one('gorev_takip.gorev_takip',string ='Görev(İsteğe Bağlı) ',required=False)