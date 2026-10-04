from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    pos_role = fields.Selection(
        [
            ('admin', 'Admin'),
            ('salesman', 'Salesman'),
            ('cashier', 'Cashier'),
        ],
        string="POS Role",
        default='salesman'
    )

    def has_pos_admin_role(self):
        self.ensure_one()
        return self.pos_role == 'admin' or self.has_group('base.group_system')
