# -*- coding: utf-8 -*-

from odoo import models, fields, api


class batarya_takip(models.Model):
    _name = 'batarya_takip.batarya_takip'
    _description = 'batarya_takip.batarya_takip'

    name = fields.Char("Batarya Kodu")
    cycle = fields.Integer("Cycle")



