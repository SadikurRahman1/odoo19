from odoo import models, fields


class Department(models.Model):

    _name = 'student_management.department'
    _description = 'Department'
    _order = 'name'

    name = fields.Char(
        string="Department Name",
        required=True
    )

    code = fields.Char(
        string="Department Code",
        required=True,
        copy=False
    )

    description = fields.Text(
        string="Description"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    program_ids = fields.One2many(
        'student_management.program',
        'department_id',
        string="Programs"
    )

    student_ids = fields.One2many(
        'student_management.student',
        'department_id',
        string="Students"
    )