from odoo import models, api, _
from odoo.exceptions import AccessError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
            raise AccessError(
                _('You are not allowed to create sales orders. Only Admin can create sales orders.')
            )
        return super().create(vals_list)

    def action_confirm(self):
        for order in self:
            if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                raise AccessError(
                    _('You are not allowed to confirm sales orders. Only Admin can confirm sales orders.')
                )
        return super().action_confirm()

    def action_cancel(self):
        for order in self:
            if not self.env.user.has_pos_admin_role() and not self.env.user.has_group('base.group_system'):
                raise AccessError(
                    _('You are not allowed to cancel sales orders. Only Admin can cancel sales orders.')
                )
        return super().action_cancel()
