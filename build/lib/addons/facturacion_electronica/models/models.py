# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class facturacion_electronica(models.Model):
#     _name = 'facturacion_electronica.facturacion_electronica'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100



class Billing(models.Model):
    _name = 'billing'
    #status = fields.Selection([('signed', 'sent', 'authorized', 'notified')])
    name = fields.Char()


