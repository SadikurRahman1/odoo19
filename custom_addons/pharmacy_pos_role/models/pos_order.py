from odoo import models, api, _
from odoo.exceptions import AccessError, UserError


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def _process_order(self, order, existing_order):
        if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
            raise AccessError(
                _('You are not allowed to process POS orders. Only Admin can process POS orders.')
            )
        return super()._process_order(order, existing_order)

    def action_pos_order_paid(self):
        for order in self:
            if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                raise AccessError(
                    _('You are not allowed to mark POS orders as paid. Only Admin can process payments.')
                )
        return super().action_pos_order_paid()

    def add_payment(self, data):
        self.ensure_one()
        payment_method = self.env['pos.payment.method'].browse(data.get('payment_method_id'))
        if payment_method and payment_method.type == 'cash':
            if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                raise UserError(
                    _('Cash payments are not allowed for your role. Only Admin can collect cash payments.')
                )
        return super().add_payment(data)

    def create_from_ui(self, orders, draft=False):
        if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
            raise AccessError(
                _('You are not allowed to create POS orders from the UI. Only Admin can create POS orders.')
            )
        return super().create_from_ui(orders, draft)
