from odoo import models, fields, api

class TaskPilot(models.Model):
    _name = 'task.pilot'
    _description = 'task.pilot'
    
    name = fields.Char("Pilot Kullanıcı Adı")
    pilotStatus = fields.Selection([('pilot','Pilot'),('copilot','Copilot'),('stajyer','Stajyer'),('bolge_sorumlusu','Bölge Sorumlusu')],string='Pilotluk Durumu',default='pilot')
    #pilot_task_ids = fields.Many2one('gorev_takip.gorev_takip',string ='Görev(İsteğe Bağlı) ',required=False)