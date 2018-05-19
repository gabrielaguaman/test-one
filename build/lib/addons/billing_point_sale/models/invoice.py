from odoo import models, fields, api

class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = ['account.invoice', 'account.edocument']












