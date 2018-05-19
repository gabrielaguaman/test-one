from odoo import models, fields, api
import random

class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Name", compute='_compute_name')
    active = fields.Boolean("Is Active")
    image = fields.Binary()
    pages = fields.Integer("Pages")
    category_id = fields.Many2one("library.category", string="Category",  default=2)

    #@api.multi
    #def _compute_name(self):
    #    for record in self:
    #        record.name = str(random.randint(1, 5))

    @api.depends('pages')
    def _compute_name(self):
        for record in self:
            record.name = "%s %s" % (record.pages, record.name)
