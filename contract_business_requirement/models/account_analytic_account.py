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
    @api.depends(
        "valid_business_requirement_ids",
        "valid_business_requirement_ids.state",
        "valid_business_requirement_ids.total_revenue",
        "valid_business_requirement_ids.resource_task_total",
        "valid_business_requirement_ids.resource_procurement_total",
        "valid_business_requirement_ids.gross_profit",
    )
    def _compute_business_requirement(self):
        for acc in self:
            deliverable_ids = []
            total_revenue = resource_task_total = \
                resource_procurement_total = gross_profit = 0.0
            for br in acc.valid_business_requirement_ids:
                deliverable_ids += br.deliverable_lines.ids
                total_revenue += br.total_revenue
                resource_task_total += br.resource_task_total
                resource_procurement_total += br.resource_procurement_total
                gross_profit += br.gross_profit
            acc.business_requirement_deliverable_ids = deliverable_ids
            acc.total_revenue = total_revenue
            acc.resource_task_total = resource_task_total
            acc.resource_procurement_total = resource_procurement_total
            acc.gross_profit = gross_profit

    @api.multi
    @api.depends(
        "total_revenue",
    )
    def _compute_fix_price_to_invoice(self):
        for aa in self:
            aa.fix_price_to_invoice = aa.total_revenue

    business_requirement_ids = fields.One2many(
        string="Business Requirements",
        comodel_name="business.requirement",
        inverse_name="analytic_id",
    )
    valid_business_requirement_ids = fields.One2many(
        string="Valid Business Requirements",
        comodel_name="business.requirement",
        inverse_name="analytic_id",
        domain=[
            ("state", "in", ["stakeholder_approval", "in_progress", "done"]),
        ]
    )
    business_requirement_deliverable_ids = fields.Many2many(
        string="Deliverables",
        comodel_name="business.requirement.deliverable",
        compute="_compute_business_requirement",
    )
    total_revenue = fields.Float(
        string="Total Revenue",
        compute="_compute_business_requirement",
        store=True,
    )
    resource_task_total = fields.Float(
        string="Total Tasks",
        compute="_compute_business_requirement",
        store=True,
    )
    resource_procurement_total = fields.Float(
        string="Total Procurement",
        compute="_compute_business_requirement",
        store=True,
    )
    gross_profit = fields.Float(
        string="Estimated Gross Profit",
        compute="_compute_business_requirement",
        store=True,
    )
    fix_price_to_invoice = fields.Float(
        compute="_compute_fix_price_to_invoice",
    )
