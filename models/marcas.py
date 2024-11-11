from odoo import models, fields, api

class Marcas_social_marketing (models.Model):
    _name = 'marcas.grilla_marketing'
    _description = 'Marcas Social Marketing'

    name = fields.Char(string='Marca', required=True)
    color = fields.Integer(string='Color')
    