from odoo import models, fields


class Program(models.Model):

    _name = 'student_management.program'
    _description = 'Academic Program'
    _order = 'name'

    name = fields.Char(
        string="Program Name",
        required=True
    )

    code = fields.Char(
        string="Program Code",
        required=True,
        copy=False
    )

    department_id = fields.Many2one(
        'student_management.department',
        string="Department",
        required=True,
        ondelete='restrict'
    )

    duration = fields.Integer(
        string="Duration (Years)"
    )

    description = fields.Text(
        string="Description"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    batch_ids = fields.One2many(
        'student_management.batch',
        'program_id',
        string="Batches"
    )

    student_ids = fields.One2many(
        'student_management.student',
        'program_id',
        string="Students"
    )