
from odoo import http


class HaritaIslemleri(http.Controller):
    

    @http.route('/harita_islemleri', auth='public')
    def list(self, **kw):
        return http.request.render('harita_islemleri.listing', {
            'root': '/harita_islemleri',
            'objects': http.request.env['harita_islemleri.harita_islemleri'].search([]),
        })

    @http.route('/harita_islemleri/<model("harita_islemleri.harita_islemleri"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('harita_islemleri.object', {
            'object': obj
        })

