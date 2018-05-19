# -*- coding: utf-8 -*-
from odoo import http

# class Addons/librayBookDate(http.Controller):
#     @http.route('/addons/libray_book_date/addons/libray_book_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/libray_book_date/addons/libray_book_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/libray_book_date.listing', {
#             'root': '/addons/libray_book_date/addons/libray_book_date',
#             'objects': http.request.env['addons/libray_book_date.addons/libray_book_date'].search([]),
#         })

#     @http.route('/addons/libray_book_date/addons/libray_book_date/objects/<model("addons/libray_book_date.addons/libray_book_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/libray_book_date.object', {
#             'object': obj
#         })