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
from odoo import models


class PosSession(models.Model):
    """ Heredando sesión pos para cargar modelos y campos """
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        """ Cargar modelo de línea de pedido pos y modelo de pedido pos """
        result = super()._pos_ui_models_to_load()
        result += {
            'pos.order', 'pos.order.line'
        }
        return result

    def _loader_params_pos_order(self):
        """ Cargar campos a la sesión pos """
        return {'search_params': {
            'domain': [],
            'fields': ['name', 'date_order', 'pos_reference',
                       'partner_id', 'lines', 'exchange']}}

    def _get_pos_ui_pos_order(self, params):
        """ Cargar pedido pos a la sesión """
        return self.env['pos.order'].search_read(
            **params['search_params'])

    def _loader_params_pos_order_line(self):
        """Cargar campos de línea de pedido pos a la sesión """
        return {'search_params': {'domain': [],
                                  'fields': ['product_id', 'qty',
                                             'price_subtotal', 'total_cost']}}

    def _get_pos_ui_pos_order_line(self, params):
        """ Obtener modelos de línea de pedido pos para la sesión pos """
        return self.env['pos.order.line'].search_read(
            **params['search_params'])
