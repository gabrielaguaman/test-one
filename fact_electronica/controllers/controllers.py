# -*- coding: utf-8 -*-
from odoo import http

# class FactElectronica(http.Controller):
#     @http.route('/fact_electronica/fact_electronica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fact_electronica/fact_electronica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fact_electronica.listing', {
#             'root': '/fact_electronica/fact_electronica',
#             'objects': http.request.env['fact_electronica.fact_electronica'].search([]),
#         })

#     @http.route('/fact_electronica/fact_electronica/objects/<model("fact_electronica.fact_electronica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fact_electronica.object', {
#             'object': obj
#         })