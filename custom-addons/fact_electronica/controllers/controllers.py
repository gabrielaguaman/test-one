# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/factElectronica(http.Controller):
#     @http.route('/custom-addons/fact_electronica/custom-addons/fact_electronica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/fact_electronica/custom-addons/fact_electronica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/fact_electronica.listing', {
#             'root': '/custom-addons/fact_electronica/custom-addons/fact_electronica',
#             'objects': http.request.env['custom-addons/fact_electronica.custom-addons/fact_electronica'].search([]),
#         })

#     @http.route('/custom-addons/fact_electronica/custom-addons/fact_electronica/objects/<model("custom-addons/fact_electronica.custom-addons/fact_electronica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/fact_electronica.object', {
#             'object': obj
#         })