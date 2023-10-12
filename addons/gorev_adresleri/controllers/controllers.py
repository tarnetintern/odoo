#-*- coding: utf-8 -*-
from odoo import http


class GorevAdresleri(http.Controller):

    @http.route('/gorev_adresleri', auth='public')
    def list(self, **kw):
        return http.request.render('gorev_adresleri.listing', {
            'root': '/gorev_adresleri',
            'objects': http.request.env['gorev_adresleri.gorev_adresleri'].search([]),
        })

    @http.route('/gorev_adresleri/<model("gorev_adresleri.gorev_adresleri"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gorev_adresleri.object', {
            'object': obj
        })
