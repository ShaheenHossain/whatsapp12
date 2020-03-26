# -*- coding: utf-8 -*-

import logging
from odoo import models, api

_logger = logging.getLogger(__name__)


class SaleOrderConfirm(models.TransientModel):
    _name = 'sale.order.confirm'
    _description = "Wizard - Sale Order Confirm/Cancel"

    @api.multi
    def sale_confirm(self):
        """filter the records of the state 'draft' and 'sent', and will confirm this and others will be skipped"""
        quotations = self._context.get('active_ids')
        quotations_ids = self.env['sale.order'].browse(quotations).\
            filtered(lambda x: x.state == 'draft' or x.state == "sent")
        for quotation in quotations_ids:
            quotation.action_confirm()

    @api.multi
    def sale_cancel(self):
        quotations = self._context.get('active_ids')
        quotations_ids = self.env['sale.order'].browse(quotations)
        for quotation in quotations_ids:
            try:
                quotation.action_cancel()
            except:
                pass





