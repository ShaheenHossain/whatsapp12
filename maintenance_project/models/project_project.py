# Copyright 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    equipment_count = fields.Integer(
        compute='_compute_equipment_count')
    equipment_ids = fields.One2many(
        'maintenance.equipment',
        'project_id',
        string='Equipments')
    maintenance_request_count = fields.Integer(
        compute='_compute_maintenance_request_count')
    maintenance_request_ids = fields.One2many(
        'maintenance.request',
        'project_id',
        string='Maintenance Requests')

    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        for project in self:
            project.equipment_count = len(project.equipment_ids)

    def action_view_equipment_ids(self):
        """
        Access to the current equipments for this project
        """
        self.ensure_one()
        action = self.env.ref('maintenance.hr_equipment_action').read()[0]
        action['domain'] = [('project_id', '=', self.id)]
        action['context'] = {
            'default_project_id': self.id,
            'default_create_project_from_equipment': False,
        }
        return action

    @api.depends('maintenance_request_ids')
    def _compute_maintenance_request_count(self):
        for project in self:
            project.maintenance_request_count = \
                len(project.maintenance_request_ids.filtered(
                    lambda x: not x.stage_id.done))

    def action_view_maintenance_request_ids(self):
        """
        Access to the undone maintenance requests for this project
        """
        self.ensure_one()
        action = self.env.ref(
            'maintenance.hr_equipment_request_action').read()[0]
        action['domain'] = [('project_id', '=', self.id),
                            ('stage_id.done', '=', False)]
        action['context'] = {
            'default_project_id': self.id,
        }
        return action
