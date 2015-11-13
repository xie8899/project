# -*- coding: utf-8 -*-
# © <YEAR(2015)>
# <AUTHOR(Elico Corp, contributor: Eric Caudal, Alex Duan, Xie XiaoPeng)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests import common


@common.at_install(False)
@common.post_install(True)
class BusinessRequirementTestCase(common.TransactionCase):
    def setUp(self):
        super(BusinessRequirementTestCase, self).setUp()
        self.br = self.env['business.requirement']

    def test_generate_tasks_wizard(self):
        vals = {
            'name': ' test',
            'rough_estimation_lines': [
                (0, 0, {'name': 'task1', 'estimated_time': 15.0}),
                (0, 0, {'name': 'task2', 'estimated_time': 25.0}),
                (0, 0, {'name': 'task3', 'estimated_time': 35.0}),
                (0, 0, {'name': 'task4', 'estimated_time': 45.0}),
            ]
        }
        br = self.br.create(vals)
        action = br.generate_tasks_wizard()
        success = False
        if action:
            success = True
        self.assertTrue(success)


@common.at_install(False)
@common.post_install(True)
class BrGenerateTasksTestCase(common.TransactionCase):
    def setUp(self):
        super(BrGenerateTasksTestCase, self).setUp()
        self.br = self.env['business.requirement']
        self.wizard = self.env['br.generate.tasks']

    def test_generate_tasks(self):
        vals = {
            'name': ' test',
            'rough_estimation_lines': [
                (0, 0, {'name': 'task1', 'estimated_time': 15.0}),
                (0, 0, {'name': 'task2', 'estimated_time': 25.0}),
                (0, 0, {'name': 'task3', 'estimated_time': 35.0}),
                (0, 0, {'name': 'task4', 'estimated_time': 45.0}),
            ]
        }
        br = self.br.create(vals)
        action = br.generate_tasks_wizard()
        wizard_id = action.get('res_id', False)
        wizard = self.wizard.browse(wizard_id)
        tasks = wizard.generate_tasks()

        success = False
        if tasks:
            success = True
        self.assertTrue(success)