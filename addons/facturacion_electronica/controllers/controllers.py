# -*- coding: utf-8 -*-
from odoo import http

# class FacturacionElectronica(http.Controller):
#     @http.route('/facturacion_electronica/facturacion_electronica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facturacion_electronica/facturacion_electronica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('facturacion_electronica.listing', {
#             'root': '/facturacion_electronica/facturacion_electronica',
#             'objects': http.request.env['facturacion_electronica.facturacion_electronica'].search([]),
#         })

#     @http.route('/facturacion_electronica/facturacion_electronica/objects/<model("facturacion_electronica.facturacion_electronica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facturacion_electronica.object', {
#             'object': obj
#         })

class Sign_Billing():
    pass

class Generate_xml():
    pass