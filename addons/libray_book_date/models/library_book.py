from odoo import models, fields, api

class LibraryBook(models.Model):

    _inherit = "library.book"

    date = fields.Date(string="Release Date", default=fields.Date.today)