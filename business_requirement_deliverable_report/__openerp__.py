# -*- coding: utf-8 -*-
# © 2016 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Business Requirement Deliverable Report Docx Module',
    'version': '9.0.1.0.1',
    'category': 'report',
    'depends': [
        'report_docx',
        'business_requirement_deliverable',
    ],
    'data': [
        'reports/business_requirement_deliverable_report.xml',
        'static/docx_templates/template_business_requirement.docx',
        'static/docx_templates/template_business_requirement_deliverable.docx',
        'static/docx_templates/template_business_requirement_deliverable_resources.docx',
    ],
    'author': 'Elico Corp',
    'license': 'AGPL-3',
    'website': 'https://www.elico-corp.com',
    'installable': True,
    'application': False
}
