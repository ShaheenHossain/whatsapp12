# Copyright 2020 ForgeFlow S.L. (https://forgeflow.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Maintenance Equipments Hierarchy',
    'summary': 'Manage equipment hierarchy',
    'author': 'ForgeFlow, Odoo Community Association (OCA)',
    'website': 'http://github.com/OCA/maintenance',
    'category': 'Equipments, Assets, Internal Hardware, Allocation Tracking',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'maintenance',
    ],
    'data': [
        'views/maintenance_equipment_views.xml',
    ],
    'demo': [
        'data/demo_maintenance_equipment_hierarchy.xml'
    ],
}
