# -*- coding: utf-8 -*-
# ©  2015-2017 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo import api
from odoo import models


class Picking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def do_new_transfer(self):
        for picking in self:
            for move in picking.move_lines:
                if not move.quantity_done_store:
                    move.quantity_done_store = move.product_qty
        return super(Picking, self).do_new_transfer()
