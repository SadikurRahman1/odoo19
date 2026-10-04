from odoo import models, api, _
from odoo.exceptions import UserError


class PosSession(models.Model):
    _inherit = 'pos.session'

    def action_pos_session_open(self):
        for session in self:
            if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                raise UserError(
                    _('Only Admin can open POS sessions.')
                )
        return super().action_pos_session_open()

    def action_pos_session_close(self):
        for session in self:
            if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                raise UserError(
                    _('Only Admin can close POS sessions.')
                )
        return super().action_pos_session_close()

    def _pos_ui_process_orders(self, order_ids):
        if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
            raise UserError(
                _('Only Admin can process POS session orders.')
            )
        return super()._pos_ui_process_orders(order_ids)
