
from odoo import http


class GorevTakip(http.Controller):
    

    @http.route('/gorev_takip', auth='public')
    def list(self, **kw):
        return http.request.render('gorev_takip.listing', {
            'root': '/gorev_takip',
            'objects': http.request.env['gorev_takip.gorev_takip'].search([]),
        })

    @http.route('/gorev_takip/<model("gorev_takip.gorev_takip"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gorev_takip.object', {
            'object': obj
        })

# GET metodu için listeleme yazılacak.

    # @http.route('/gorev_takip/adresler',auth='public')
    # def addresslist(self,**kw):
    #     return http.request.render('gorev_adres.listing', {
    #         'root': '/gorev_takip/adresler',
    #         'objects': http.request.env['gorev.adres'].search([]),
    #     })
    # @http.route('/gorev_takip/adresler/<model("gorev.adres"):obj>', auth='public')
    # def adressobject(self, obj, **kw):
    #     return http.request.render('gorev.adres.object', {
    #         'object': obj
    #     })
    
    # @http.route('/gorev_takip/ilaclar',auth='public')
    # def ilaclist(self,**kw):
    #     return http.request.render('task.medicine.listing', {
    #         'root': '/gorev_takip/ilaclar',
    #         'objects': http.request.env['task.medicine'].search([]),
    #     })
    
    # @http.route('/gorev_takip/ilaclar/<model("task.medicine"):obj>', auth='public')
    # def adressobject(self, obj, **kw):
    #     return http.request.render('task.medicine.object', {
    #         'object': obj
    #     })