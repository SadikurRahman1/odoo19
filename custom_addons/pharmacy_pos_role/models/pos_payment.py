from odoo import models, api, _
from odoo.exceptions import UserError


class PosPayment(models.Model):
    _inherit = 'pos.payment'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            payment_method = self.env['pos.payment.method'].browse(vals.get('payment_method_id'))
            if payment_method and payment_method.type == 'cash':
                if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                    raise UserError(
                        _('Cash payments are not allowed for your role. Only Admin can collect cash payments.')
                    )
        return super().create(vals_list)

    def _create_payment_moves(self, is_reverse=False):
        for payment in self:
            if payment.payment_method_id.type == 'cash':
                if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                    raise UserError(
                        _('Cash payment moves cannot be created for your role. Only Admin can process cash payments.')
                    )
        return super()._create_payment_moves(is_reverse)
