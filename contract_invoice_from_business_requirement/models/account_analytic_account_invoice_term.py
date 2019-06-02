# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AccountAnalyticAccountInvoiceTerm(models.Model):
    _name = "account.analytic_account_invoice_term"
    _description = "Invoice Term From Business Requirement"
    _order = "sequence, id"

    @api.multi
    @api.depends(
        "analytic_account_id",
        "analytic_account_id.total_revenue",
        "percentage",
    )
    def _compute_amount(self):
        for line in self:
            line.term_amount = (line.percentage / 100.00) * \
                line.analytic_account_id.total_revenue

    analytic_account_id = fields.Many2one(
        string="# Contract",
        comodel_name="account.analytic.account",
    )
    partner_id = fields.Many2one(
        string="Customer",
        comodel_name="res.partner",
        related="analytic_account_id.partner_id.commercial_partner_id",
        store=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    product_id = fields.Many2one(
        string="Use This Product For Invoice",
        comodel_name="product.product",
        domain=[
            ("type", "=", "service"),
        ],
    )
    name = fields.Char(
        string="Term",
        required=True,
    )
    percentage = fields.Float(
        string="Percentage",
        required=True,
    )
    term_amount = fields.Float(
        string="Term Amount",
        compute="_compute_amount",
        store=False,
    )
    invoice_line_id = fields.Many2one(
        string="Invoice Line",
        comodel_name="account.invoice.line",
        readonly=True,
    )
    invoice_id = fields.Many2one(
        string="# Invoice",
        comodel_name="account.invoice",
        related="invoice_line_id.invoice_id",
        store=True,
    )
