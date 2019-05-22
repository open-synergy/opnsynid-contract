# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = [
        "account.analytic.account",
    ]

    fix_price_payment_term_id = fields.Many2one(
        string="Payment Term for Fixed Price",
        comodel_name="account.payment.term",
    )
    fix_price_bank_account_id = fields.Many2one(
        string="Bank Account for Fixed Price",
        comodel_name="res.partner.bank",
    )
