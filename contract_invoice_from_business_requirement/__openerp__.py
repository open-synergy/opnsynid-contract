# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Invoice From Business Requirement",
    "version": "8.0.1.0.0",
    "category": "Business Requirements Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "contract_business_requirement",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/create_invoice_from_term.xml",
        "views/account_analytic_account_views.xml",
    ],
}
