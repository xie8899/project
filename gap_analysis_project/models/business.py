# -*- coding: utf-8 -*-
# © <YEAR(2015)>
# <AUTHOR(Elico Corp, contributor: Eric Caudal, Alex Duan, Xie XiaoPeng)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class BusinessRequirement(models.Model):
    _inherit = "business.requirement"

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
        ondelete='set null'
    )
    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name='br_id',
        string='Tasks',
        copy=False
    )

    @api.multi
    def generate_project_wizard(self):
        vals = {
            'br_id': self.id,
        }
        wizard_obj = self.env['br.generate.project']
        wizard = wizard_obj.create(vals)
        action = wizard.wizard_view()
        return action

    @api.multi
    def update_project_id(self, project_id):
        for br in self:
            br.project_id = project_id

    @api.multi
    def generate_tasks_wizard(self):
        lines = []
        for line in self.rough_estimation_lines:
            line = (
                0, 0,
                {
                    'name': line.name,
                    'sequence': line.sequence,
                    'estimated_time_total': line.estimated_time,
                    'select': True,
                }
            )
            lines.append(line)

        vals = {
            'project_id': self.project_id.id,
            'br_id': self.id,
            'lines': lines,
        }
        wizard_obj = self.env['br.generate.tasks']
        wizard = wizard_obj.create(vals)
        action = wizard.wizard_view()
        return action


class Project(models.Model):
    _inherit = "project.project"

    br_ids = fields.One2many(
        comodel_name='business.requirement',
        inverse_name='project_id',
        string='Business Analysis',
        copy=False,
    )
    br_count = fields.Integer(
        compute='_br_count',
        string="Bus. Req. Number"
    )

    @api.one
    @api.depends('br_ids')
    def _br_count(self):
        self.br_count = len(self.br_ids)


class ProjectTask(models.Model):
    _inherit = "project.task"

    br_id = fields.Many2one(
        comodel_name='business.requirement',
        string='Business Analysis',
        ondelete='set null'
    )