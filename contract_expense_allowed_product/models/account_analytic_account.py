# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = [
        "account.analytic.account",
    ]

    limit_expense_product = fields.Boolean(
        string="Limit Expense Product",
    )
    expense_allowed_product_ids = fields.One2many(
        string="Expense Allowed Products",
        comodel_name="account.analytic_account_expense_allowed_product",
        inverse_name="analytic_account_id",
    )
