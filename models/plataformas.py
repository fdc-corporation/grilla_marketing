from odoo import models, fields, api

class Plataformas_social_marketing (models.Model):
    _name = 'plataformas.grilla_marketing'
    _description = 'Plataformas social marketing'
    name = fields.Char(string='Marca', required=True)
    color = fields.Integer(string='Color')


