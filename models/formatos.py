from odoo import models, fields, api


class Formatos (models.Model):
    _name = 'formatos.grilla_marketing'
    _description = 'Formatos de publicacion'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')




