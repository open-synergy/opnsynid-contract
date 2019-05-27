# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class CreateInvoiceFromTerm(models.TransientModel):
    _name = "account.create_invoice_from_term"
    _description = "Create Invoice From Invoice Term"

    @api.model
    def _default_invoice_term_id(self):
        return self._context.get("active_id", False)

    @api.multi
    @api.depends(
        "invoice_term_id",
    )
    def _compute_contract_partner_id(self):
        for wiz in self:
            result = False
            aa = wiz.invoice_term_id.analytic_account_id
            if aa.partner_id:
                result = aa.partner_id.commercial_partner_id.id
            wiz.contract_partner_id = result

    invoice_term_id = fields.Many2one(
        string="Invoice Term",
        comodel_name="account.analytic_account_invoice_term",
        default=lambda self: self._default_invoice_term_id(),
    )
    contract_partner_id = fields.Many2one(
        string="Contract Partner",
        comodel_name="res.partner",
        compute="_compute_contract_partner_id",
        store=False,
    )
    partner_id = fields.Many2one(
        string="Invoice To",
        comodel_name="res.partner",
        required=True,
    )
    journal_id = fields.Many2one(
        string="Journal",
        comodel_name="account.journal",
        required=True,
        domain=[
            ("type", "=", "sale"),
        ],
    )
    date_invoice = fields.Date(
        string="Date Invoice",
        required=True,
    )
    due_mode = fields.Selection(
        string="Due Date Mode",
        selection=[
            ("payment_term", "By Payment Term"),
            ("due_date", "By Due Date"),
        ],
        required=True,
        default="due_date",
    )
    payment_term_id = fields.Many2one(
        string="Payment Term",
        comodel_name="account.payment.term",
    )
    due_date = fields.Date(
        string="Due Date",
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._create_invoice()

    @api.multi
    def _create_invoice(self):
        self.ensure_one()
        obj_invoice = self.env["account.invoice"]
        invoice = obj_invoice.create(self._prepare_invoice())
        line = self._create_invoice_line(invoice)
        invoice.button_reset_taxes()
        self.invoice_term_id.write({
            "invoice_line_id": line.id,
        })

    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        return {
            "partner_id": self.partner_id.id,
            "type": "out_invoice",
            "date_invoice": self.date_invoice,
            "date_due": self.due_date,
            "payment_term": self.payment_term_id and
            self.payment_term_id.id or False,
            "journal_id": self.journal_id.id,
            "user_id": self.env.user.id,
            "account_id": self.partner_id.property_account_receivable.id,
            "currency_id": self.invoice_term_id.analytic_account_id.
            currency_id.id,
        }

    @api.multi
    def _create_invoice_line(self, invoice):
        self.ensure_one()
        obj_line = self.env["account.invoice.line"]
        line = obj_line.create(self._prepare_invoice_line(invoice))
        return line

    @api.multi
    def _prepare_invoice_line(self, invoice):
        self.ensure_one()
        return {
            "invoice_id": invoice.id,
            "product_id": self.invoice_term_id.product_id.id,
            "name": self.invoice_term_id.name,
            "account_id": self.invoice_term_id.product_id.
            property_account_income.id,
            "account_analytic_id": self.invoice_term_id.analytic_account_id.id,
            "price_unit": self.invoice_term_id.term_amount,
            "invoice_line_tax_id":
            [(6, 0, self.invoice_term_id.product_id.taxes_id.ids)],
        }
