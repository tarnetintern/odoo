# -*- coding: utf-8 -*-
from odoo import http


class GorevIlaclari(http.Controller):


    @http.route('/gorev_ilaclari', auth='public')
    def list(self, **kw):
        return http.request.render('gorev_ilaclari.listing', {
            'root': '/gorev_ilaclari',
            'objects': http.request.env['gorev_ilaclari.gorev_ilaclari'].search([]),
        })

    @http.route('/gorev_ilaclari/<model("gorev_ilaclari.gorev_ilaclari"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gorev_ilaclari.object', {
            'object': obj
        })
