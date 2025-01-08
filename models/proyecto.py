from odoo import models, fields, api
from datetime import datetime


class Proyecto(models.Model):
    _inherit = "project.task"

    responsable = fields.Many2many(
        "responsables.grilla_marketing", string="Responsables"
    )
    marcas = fields.Many2many("marcas.grilla_marketing", string="Marcas")
    plataformas = fields.Many2many("plataformas.grilla_marketing", string="Plataformas")
    formatos = fields.Many2many("formatos.grilla_marketing", string="Formatos")
    guion = fields.Html(string="Guion")
    evento_id = fields.Many2one("calendar.event", string="Evento en calendario")

    def create_evento_tarea(self):
        try:
            for record in self:
                plataformas_id = []
                for plataforma in record.plataformas:
                    plataformas_id.append(plataforma.id)

                if record.date_deadline:
                    evento = self.env["calendar.event"].create(
                        {
                            "name": record.name + " - " + record.project_id.name,
                            "start": record.date_deadline,
                            "stop": record.date_deadline,
                            "grilla_id": record.id,
                            "partner_ids": [self.env.user.partner_id.id],
                            "plataformas": [(6, 0, plataformas_id)],
                        }
                    )
                    self.write(
                        {
                            "evento_id": evento.id,
                        }
                    )
                else:
                    raise UserError(_("Debe especificar una fecha de programacion"))
        except Exception as e:
            raise UserError(_("No se pudo ejecutar la tarea"))

    def set_notification(self):
        for record in self:
            if task.date_deadline == fields.Datetime.now():
                print(
                    "------------------------SE ENVIO LA NOTIFICACION-------------------------"
                )

                # Crear la notificación
                task.message_post(
                    body="¡La tarea ha alcanzado la fecha de vencimiento!",
                    message_type="notification",
                    subtype_xmlid="mail.mt_comment",
                )
            print(
                "------------------------FECHA DE VENCIMIENTO-------------------------"
            )
            print(task.date_deadline)
            print(fields.Datetime.now())
 