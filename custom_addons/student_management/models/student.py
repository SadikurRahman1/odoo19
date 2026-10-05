from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class Student(models.Model):

    _name = 'student_management.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student'
    _order = 'name'
    _rec_name = 'name'

    # =========================================================
    # Basic Information
    # =========================================================

    name = fields.Char(
        string="Full Name",
        required=True,
        tracking=True
    )

    student_id = fields.Char(
        string="Student ID",
        required=True,
        copy=False,
        tracking=True
    )

    photo = fields.Image(
        string="Photo",
        tracking=True
    )

    email = fields.Char(
        string="Email",
        tracking=True
    )

    phone = fields.Char(
        string="Phone",
        tracking=True
    )

    # =========================================================
    # Personal Information
    # =========================================================

    date_of_birth = fields.Date(
        string="Date of Birth",
        tracking=True
    )

    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
        readonly=True
    )

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        string="Gender",
        tracking=True
    )

    blood_group = fields.Selection(
        [
            ('a+', 'A+'),
            ('a-', 'A-'),
            ('b+', 'B+'),
            ('b-', 'B-'),
            ('o+', 'O+'),
            ('o-', 'O-'),
            ('ab+', 'AB+'),
            ('ab-', 'AB-'),
        ],
        string="Blood Group",
        tracking=True
    )

    address = fields.Text(
        string="Address",
        tracking=True
    )

    # =========================================================
    # Academic Information
    # =========================================================

    department_id = fields.Many2one(
        'student_management.department',
        string="Department",
        ondelete='restrict'
    )

    department_code = fields.Char(
        string="Department",
        related="department_id.code",
        store=True,
        readonly=True
    )

    program_id = fields.Many2one(
        'student_management.program',
        string="Program",
        ondelete='restrict'
    )

    program_code = fields.Char(
        string="Program",
        related="program_id.code",
        store=True,
        readonly=True
    )

    batch_id = fields.Many2one(
        'student_management.batch',
        string="Batch",
        ondelete='restrict'
    )

    batch_code = fields.Char(
        string="Batch",
        related="batch_id.code",
        store=True,
        readonly=True
    )

    semester = fields.Selection(
        [
            ('1', '1st Semester'),
            ('2', '2nd Semester'),
            ('3', '3rd Semester'),
            ('4', '4th Semester'),
            ('5', '5th Semester'),
            ('6', '6th Semester'),
            ('7', '7th Semester'),
            ('8', '8th Semester'),
        ],
        string="Current Semester"
    )

    admission_date = fields.Date(
        string="Admission Date"
    )

    # =========================================================
    # Guardian Information
    # =========================================================

    guardian_name = fields.Char(
        string="Guardian Name"
    )

    guardian_phone = fields.Char(
        string="Guardian Phone"
    )

    guardian_relation = fields.Selection(
        [
            ('father', 'Father'),
            ('mother', 'Mother'),
            ('guardian', 'Guardian'),
        ],
        string="Guardian Relation"
    )

    note = fields.Text(string="Notes")
    
    # =========================================================
    # Student Status
    # =========================================================
    
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('complete', 'Complete'),
        ],
        string="Stage",
        default="draft",
        required=True,
        tracking=True
)

    status = fields.Selection(
        [
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('graduated', 'Graduated'),
            ('dropped', 'Dropped'),
        ],
        string="Status",
        default="active",
        required=True
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    # =========================================================
    # Age Calculation
    # =========================================================

    @api.depends('date_of_birth')
    def _compute_age(self):

        today = date.today()

        for student in self:

            if student.date_of_birth:

                dob = student.date_of_birth

                age = today.year - dob.year

                if (today.month, today.day) < (dob.month, dob.day):
                    age -= 1

                student.age = age

            else:

                student.age = 0

    # =========================================================
    # Date of Birth Validation
    # =========================================================

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):

        today = date.today()

        for student in self:

            if not student.date_of_birth:
                continue

            # DOB cannot be in the future

            if student.date_of_birth > today:

                raise ValidationError(
                    "Date of Birth cannot be in the future."
                )

            # Calculate age

            dob = student.date_of_birth

            age = today.year - dob.year

            if (today.month, today.day) < (dob.month, dob.day):
                age -= 1

            # Minimum age validation

            if age < 16:

                raise ValidationError(
                    "Student age must be at least 16 years."
                )

            # Maximum age validation

            if age > 60:

                raise ValidationError(
                    "Student age cannot be more than 60 years."
                )

    def action_complete(self):
        for student in self:

            if not student.name:
                raise ValidationError(
                    "Student Name is required."
                )

            if not student.student_id:
                raise ValidationError(
                    "Student ID is required."
                )

            if not student.department_id:
                raise ValidationError(
                    "Department is required."
                )

            if not student.program_id:
                raise ValidationError(
                    "Program is required."
                )

            if not student.batch_id:
                raise ValidationError(
                    "Batch is required."
                )

            student.state = 'complete'


    def action_reset_to_draft(self):
        for student in self:
            student.state = 'draft'