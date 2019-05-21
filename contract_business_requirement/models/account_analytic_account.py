# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = [
        "account.analytic.account",
    ]

    @api.multi
    def _compute_business_requirement(self):
        obj_project = self.env["project.project"]
        for acc in self:
            br_ids = []
            deliverable_ids = []
            criteria = [
                ("analytic_account_id", "=", acc.id)
            ]
            projects = obj_project.search(criteria)
            for project in projects:
                br_ids += project.br_ids.ids
                for br in project.br_ids:
                    deliverable_ids += br.deliverable_lines.ids
            acc.business_requirement_ids = br_ids
            acc.business_requirement_deliverable_ids = deliverable_ids

    business_requirement_ids = fields.Many2many(
        string="Business Requirements",
        comodel_name="business.requirement",
        compute="_compute_business_requirement",
    )
    business_requirement_deliverable_ids = fields.Many2many(
        string="Deliverables",
        comodel_name="business.requirement.deliverable",
        compute="_compute_business_requirement",
    )
