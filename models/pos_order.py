# -*- coding: utf-8 -*-
#############################################################################
#
#    RENACE.TECH
#
#    Copyright (C) 2024-TODAY RENACE.TECH(<https://www.renace.tech>)
#    Author: Adderly Marte (Contact : adderlymarte@renace.tech)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models


class PosOrderLine(models.Model):
    """Heredando el modelo de línea de pedido pos para obtener detalles del producto"""
    _inherit = "pos.order.line"

    @api.model
    def get_product_details(self, ids):
        """Función para obtener los detalles del producto"""
        return [{
            'product_id': rec.product_id.id,
            'name': rec.product_id.name,
            'qty': rec.qty
        } for rec in self.browse(ids)]


class PosOrder(models.Model):
    """ Heredando el modelo de pedido pos para configurar el pedido de intercambio pos """
    _inherit = 'pos.order'

    exchange = fields.Boolean(string="Intercambio",
                              help="Indica si esta línea de pedido contiene"
                                   " productos intercambiados.")

    @api.model
    def get_pos_orders(self):
        return [{
            'id': rec.id,
            'pos_reference': rec.pos_reference,
            'name': rec.name,
            'partner_id': rec.partner_id.name if rec.partner_id else '',
            'date_order': rec.date_order,
            'lines': rec.lines.ids,
        } for rec in self.sudo().search([('exchange', '=', False)])]

