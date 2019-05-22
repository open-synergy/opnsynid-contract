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
            total_revenue = resource_task_total = \
                resource_procurement_total = gross_profit = 0.0
            criteria = [
                ("analytic_account_id", "=", acc.id)
            ]
            projects = obj_project.search(criteria)
            for project in projects:
                br_ids += project.br_ids.ids
                for br in project.br_ids:
                    deliverable_ids += br.deliverable_lines.ids
                    total_revenue += br.total_revenue
                    resource_task_total += br.resource_task_total
                    resource_procurement_total += br.resource_procurement_total
                    gross_profit += br.gross_profit
            acc.business_requirement_ids = br_ids
            acc.business_requirement_deliverable_ids = deliverable_ids
            acc.total_revenue = total_revenue
            acc.resource_task_total = resource_task_total
            acc.resource_procurement_total = resource_procurement_total
            acc.gross_profit = gross_profit

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
    total_revenue = fields.Float(
        string="Total Revenue",
        compute="_compute_business_requirement",
        store=False,
    )
    resource_task_total = fields.Float(
        string="Total Tasks",
        compute="_compute_business_requirement",
        store=False,
    )
    resource_procurement_total = fields.Float(
        string="Total Procurement",
        compute="_compute_business_requirement",
        store=False,
    )
    gross_profit = fields.Float(
        string="Estimated Gross Profit",
        compute="_compute_business_requirement",
        store=False,
    )
