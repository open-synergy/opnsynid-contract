# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = [
        "account.analytic.account",
    ]

    invoice_term_ids = fields.One2many(
        string="Invoice Terms",
        comodel_name="account.analytic_account_invoice_term",
        inverse_name="analytic_account_id",
    )
    fix_invoice_br = fields.Boolean(
        string="Fix Invoice From Business Requirement",
    )
    fix_invoice_br_mode = fields.Selection(
        string="Invoice From Business Requirement Mode",
        selection=[
            ("term", "Terms"),
            ("deliverable", "Deliverables"),
        ],
    )

    @api.onchange("fix_invoice_br")
    def onchange_fix_invoice_br_mode(self):
        if not self.fix_invoice_br:
            self.fix_invoice_br_mode = False
