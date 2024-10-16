# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{  # noqa: B018
    "name": "Camptocamp tools",
    "version": "18.0.1.0.0",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "category": "Others",
    "depends": [
        "base",
        "web",
    ],
    "external_dependencies": {
        "python": ["psycopg2"],
    },
    "website": "https://github.com/camptocamp/odoo-tools",
    "data": [
        "templates/camptocamp_version_template.xml",
        "views/camptocamp_version.xml",
    ],
    "installable": True,
    "auto_install": True,
}
