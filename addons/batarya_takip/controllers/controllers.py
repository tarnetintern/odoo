# -*- coding: utf-8 -*-
from odoo import http


class BataryaTakip(http.Controller):

    @http.route('/batarya_takip', auth='public')
    def list(self, **kw):
        return http.request.render('batarya_takip.listing', {
            'root': '/batarya_takip',
            'objects': http.request.env['batarya_takip.batarya_takip'].search([]),
        })

    @http.route('/batarya_takip/<model("batarya_takip.batarya_takip"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('batarya_takip.object', {
            'object': obj
        })
