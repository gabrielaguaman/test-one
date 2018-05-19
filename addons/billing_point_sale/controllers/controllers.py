# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/billingPointSale(http.Controller):
#     @http.route('/custom-addons/billing_point_sale/custom-addons/billing_point_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/billing_point_sale/custom-addons/billing_point_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/billing_point_sale.listing', {
#             'root': '/custom-addons/billing_point_sale/custom-addons/billing_point_sale',
#             'objects': http.request.env['custom-addons/billing_point_sale.custom-addons/billing_point_sale'].search([]),
#         })

#     @http.route('/custom-addons/billing_point_sale/custom-addons/billing_point_sale/objects/<model("custom-addons/billing_point_sale.custom-addons/billing_point_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/billing_point_sale.object', {
#             'object': obj
#         })