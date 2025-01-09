from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
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
        for record in self.env["project.task"].search([("date_deadline", "!=", False)]):
            fecha_original = record.date_deadline
            fecha_modificada = fecha_original - relativedelta(days=1)

            # Comparar solo las fechas sin las horas
            if fecha_modificada.date() == fields.Datetime.now().date():
                print("------------------------SE ENVIO LA NOTIFICACION-------------------------")
                message = "¡La tarea ha alcanzado la fecha de vencimiento!"
                partner_ids = [seguidor.id for seguidor in record.user_ids]
                # Crear la notificación
                record.message_post(
                    body="¡La tarea ha alcanzado la fecha de vencimiento!",
                    message_type="notification",
                    subtype_xmlid="mail.mt_comment",
                )
                record.message_notify(
                    body=message,
                    partner_ids=partner_ids,
                    subject=f"La Tarea {record.name} esta en la fecha limite!!",
                )

            # Debug de las fechas
            print("------------------------FECHA DE VENCIMIENTO-------------------------")
            print(fecha_modificada.date())  # Solo la parte de la fecha
            print(fecha_original)
            print(fields.Datetime.now().date())  # Solo la parte de la fecha
