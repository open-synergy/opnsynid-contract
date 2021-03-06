# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Contract's Business Requirement Information",
    "version": "8.0.2.1.1",
    "category": "Business Requirements Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "business_requirement_deliverable_cost",
        "account_analytic_analysis",
    ],
    "data": [
        "views/account_analytic_account_views.xml",
        "views/business_requirement_views.xml",
    ],
}
