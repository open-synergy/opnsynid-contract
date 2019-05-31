# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class BusinessRequirement(models.Model):
    _name = "business.requirement"
    _inherit = [
        "business.requirement",
    ]

    analytic_id = fields.Many2one(
        string="Master Contract",
        comodel_name="account.analytic.account",
        related="project_id.analytic_account_id",
        store=True,
        readonly=True,
    )
