# -*- coding: utf-8 -*-
# from odoo import http


# class GrillasMarketing(http.Controller):
#     @http.route('/grillas_marketing/grillas_marketing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grillas_marketing/grillas_marketing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('grillas_marketing.listing', {
#             'root': '/grillas_marketing/grillas_marketing',
#             'objects': http.request.env['grillas_marketing.grillas_marketing'].search([]),
#         })

#     @http.route('/grillas_marketing/grillas_marketing/objects/<model("grillas_marketing.grillas_marketing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grillas_marketing.object', {
#             'object': obj
#         })
