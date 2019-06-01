# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Contract Expense Allowed Product",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "category": "Hidden/Dependency",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "analytic_contract_hr_expense",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_analytic_account_views.xml",
    ],
}
