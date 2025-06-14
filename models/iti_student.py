from odoo import models, fields, api


class ITIStudent(models.Model):
    _name = "iti.student"

    # _rec_name = "age"
    name = fields.Char()
    age = fields.Integer()
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()

    salary = fields.Float()
    is_working = fields.Boolean("")
    cv = fields.Html()

    track_id = fields.Many2one('iti.track')
    track_capacity = fields.Integer(related='track_id.capacity')
    track_is_opened = fields.Boolean(related='track_id.is_opened')

    @api.onchange('is_working')
    def change_working_state(self):
        self.salary = 50000
        return {
            'warning': {
                'title': ('Change State'),
                'message': 'Working State is Changed to %s'%(self.is_working)
            }
        }

    def approve_action(self):
        self.salary = 50000
        print("in function")
