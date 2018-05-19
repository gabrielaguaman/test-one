from odoo import models, fields, api

class Bill(models.Model):
    _name = "reg.bill"
    _description = "Facturacion"

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    fecha = fields.Date(string="fecha de nacimiento")
    foto = fields.Binary(string="Foto")
    description = fields.Text(string="Descripcion")