from odoo import models, fields, api

class Responsables (models.Model):
    _name = 'responsables.grilla_marketing'
    _description = 'Responsables Social Marketing'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')







