#-*- coding: utf-8 -*-
from odoo import http


class gorevUpload(http.Controller):

    @http.route('/gorev_upload', auth='public')
    def list(self, **kw):
        return http.request.render('gorev_upload.listing', {
            'root': '/gorev_upload',
            'objects': http.request.env['gorev_upload.gorev_upload'].search([]),
        })

    @http.route('/gorev_upload/<model("gorev_upload.gorev_upload"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gorev_upload.object', {
            'object': obj
        })

@http.route('/download/<model>/<field>/<int:id>', type='http', auth="public")
def download_binary_file(self, model, field, id, **kwargs):
    print("merhabalar ben bir yerlerden biriyim")
    record = request.env[model].browse(id)
    file_content = getattr(record, field, None)
    if file_content:
        file_name = record.dosya_adi if record.dosya_adi else 'indirilen_dosya'
        return request.make_response(
            file_content,
            [('Content-Type', 'application/octet-stream'),
             ('Content-Disposition', 'attachment; filename="%s"' % file_name)]
        )
    else:
        return 'Dosya bulunamadı veya erişim hakkınız yok', 404
