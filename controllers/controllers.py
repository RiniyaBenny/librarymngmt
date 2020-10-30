# -*- coding: utf-8 -*-
from odoo import http


# class Librarymngmt(http.Controller):
#     @http.route('/librarymngmt/librarymngmt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/librarymngmt/librarymngmt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('librarymngmt.listing', {
#             'root': '/librarymngmt/librarymngmt',
#             'objects': http.request.env['librarymngmt.librarymngmt'].search([]),
#         })

#     @http.route('/librarymngmt/librarymngmt/objects/<model("librarymngmt.librarymngmt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('librarymngmt.object', {
#             'object': obj
#         })
