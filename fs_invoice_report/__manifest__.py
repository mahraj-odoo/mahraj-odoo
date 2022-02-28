# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    "name": "Invoice Report",
    "version": "15.0.0.0",
    "category": "Accounting",
    "sequence": 14,
    "summary": "",
    "author": "Fidobe",
    "website": "https://www.livbuzz.com",
    "images": [],
    "depends": ["base", "sale", "sale_management", "account", "stock"],
    "data": [
        'views/inherited_views.xml',
        "report/invoice_report.xml",
        "report/report_external_layout_bold.xml",
        "report/fs_report_invoice.xml",
        "report/fs_report_quotation.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
