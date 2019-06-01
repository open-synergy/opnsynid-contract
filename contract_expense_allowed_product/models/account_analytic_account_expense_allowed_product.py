# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccountExpenseAllowedProduct(models.Model):
    _name = "account.analytic_account_expense_allowed_product"
    _description = "Contract Allowed Expense Product"

    analytic_account_id = fields.Many2one(
        string="# Contract",
        comodel_name="account.analytic.account",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    fix_price_unit = fields.Boolean(
        string="Fix Price Unit",
    )
    price_unit = fields.Float(
        string="Price Unit",
    )
