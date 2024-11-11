from odoo import api, models, fields
from odoo.exceptions import UserError


class EventoCalendario (models.Model):
    _inherit = 'calendar.event'
    
    grilla_id = fields.Many2one('project.task', string='Grilla')
    plataformas = fields.Many2many('plataformas.grilla_marketing', string ="Plataformas")

