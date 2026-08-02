from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    pos_role = fields.Selection(
        [
            ('salesman', 'Salesman'),
            ('cashier', 'Cashier'),
        ],
        string="POS Role",
        default='salesman'
    )