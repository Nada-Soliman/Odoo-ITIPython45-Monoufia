from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class ITIStudent(models.Model):
    _name = "iti.student"

    # _rec_name = "age"
    name = fields.Char()
    age = fields.Integer(compute="compute_age", store=True)
    graduate_age = fields.Integer(compute="compute_age", store=True)
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

    levels = fields.Selection([('level1','Level1'),('level2','Level2'),('level3','Level3')])

    level_logs = fields.One2many('iti.student.log','student_id')

    roll_id = fields.Integer()

    _sql_constraints = [('unique_roll_id','UNIQUE(roll_id)','Roll Id must be unique for each student')]

    # @api.onchange('is_working')
    # def change_working_state(self):
    #     self.salary = 50000
    #     return {
    #         'warning': {
    #             'title': ('Change State'),
    #             'message': 'Working State is Changed to %s'%(self.is_working)
    #         }
    #     }


    def approve_action(self):
        self.salary = 50000
        self.levels = "level3"
        print("in function")


    def create_level_log(self):
        vals = {
            'description':'Level Changed to %s'%(self.levels),
            'student_id': self.id
        }
        self.env['iti.student.log'].create(vals)

    def write(self,vals):
        res = super(ITIStudent,self).write(vals)
        print("in write")
        if 'levels' in vals:
            for rec in self:
                rec.create_level_log()
        return res

    # @api.constrains('age')
    # def check_age(self):
    #     if self.age < 0:
    #         raise ValidationError("Age can't be negative number")
    #     elif self.age == 0:
    #         raise ValidationError("Age can't be zero")

    @api.constrains('salary','is_working')
    def check_salary(self):
        if self.is_working == True:
            if self.salary < 10000:
                raise ValidationError("Salary can't be less than 10000")

    @api.depends('age', 'graduate_age', 'birth_date')
    def compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)
                )
                rec.graduate_age = rec.age + 5
                print(f"Computed age for {rec.name}: {rec.age}")
            else:
                rec.age = 0
                rec.graduate_age = rec.age + 5
