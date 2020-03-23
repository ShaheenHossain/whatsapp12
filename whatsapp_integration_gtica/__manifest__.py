# -*- coding: utf-8 -*-
# Copyright 2019 GTICA C.A. - Ing Henry Vivas

{
    'name': 'Whatsapp Integration',
    'summary': 'Integration Whatsapp for Sale, Invoice, Delivery and more',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'author': 'GTICA C.A',
    'support': 'controlwebmanager@gmail.com',
    'license': 'OPL-1',
    'website': 'http://gtica.com.ve/',
    'price': 120.00,
    'currency': 'EUR',
    'depends': [
        'base',
        'sale_management',
        'sales_team',
        'account',
        'stock',
    ],
    'data': [
        'data/data_whatsapp_default.xml',
        'security/ir.model.access.csv',
        'views/view_whatsapp_integration.xml',
        'views/view_integration_partner.xml',
        'views/view_integration_invoice.xml',
        'views/view_integration_sale.xml',
        'views/view_integration_stock_picking.xml',
        'wizard/wizard_whatsapp_integration.xml',
        'templates/templates.xml'
    ],
    'images': ['static/description/main_screenshot.png'],
    'application': True,
    'installable': True,
}
