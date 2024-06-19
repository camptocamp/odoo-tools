# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    @api.model
    def has_camptocamp_version(self, version):
        query = "SELECT 1 FROM marabunta_version WHERE number = %s;"
        self.env.cr.execute(query, (version,))
        return bool(self.env.cr.fetchone())

    @api.model
    def latest_camptocamp_version(self):
        query = "SELECT number FROM marabunta_version ORDER BY date_done DESC LIMIT 1;"
        self.env.cr.execute(query)
        (latest_version,) = self.env.cr.fetchone()
        return latest_version
