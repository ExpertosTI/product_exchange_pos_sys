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
{
    'name': 'Intercambio de Productos POS',
    'version': '17.0.1.0.0',
    'category': 'Punto de Venta',
    'summary': """ Permite a los clientes intercambiar sus productos """,
    'description': """ Este módulo permite a los clientes devolver o intercambiar 
     sus productos """,
    'author': 'RENACE.TECH',
    'company': 'RENACE.TECH',
    'maintainer': 'RENACE.TECH',
    'website': 'https://www.renace.tech',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_order_views.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'product_exchange_pos_sys/static/src/js/all_order_screen.js',
            'product_exchange_pos_sys/static/src/xml/all_order_screen.xml',
            'product_exchange_pos_sys/static/src/js/order_button.js',
            'product_exchange_pos_sys/static/src/xml/order_button.xml',
            'product_exchange_pos_sys/static/src/js/exchange_order.js',
            'product_exchange_pos_sys/static/src/xml/exchange_order.xml',
            'product_exchange_pos_sys/static/src/scss/pos.scss'
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
