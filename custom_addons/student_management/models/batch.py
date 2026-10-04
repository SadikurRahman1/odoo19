from odoo import models, fields, api


class Batch(models.Model):

    _name = 'student_management.batch'
    _description = 'Student Batch'
    _order = 'start_date desc'

    # Basic Information

    name = fields.Char(
        string="Batch Name",
        required=True
    )

    code = fields.Char(
        string="Batch Code",
        required=True,
        copy=False
    )

    # Academic Information

    program_id = fields.Many2one(
        'student_management.program',
        string="Program",
        required=True,
        ondelete='restrict'
    )

    start_date = fields.Date(
        string="Start Date",
        required=True
    )

    end_date = fields.Date(
        string="End Date",
        compute="_compute_end_date",
        store=True,
        readonly=True
    )

    # Additional Information

    description = fields.Text(
        string="Description"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    # Student Relationship

    student_ids = fields.One2many(
        'student_management.student',
        'batch_id',
        string="Students"
    )

    # Computed End Date

    @api.depends('start_date', 'program_id.duration')
    def _compute_end_date(self):

        for record in self:

            if record.start_date and record.program_id.duration:

                record.end_date = fields.Date.add(
                    record.start_date,
                    years=record.program_id.duration
                )

            else:

                record.end_date = False