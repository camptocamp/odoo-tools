# Copyright 2026 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models
from odoo.tools.sql import drop_index

QUERY_NOT_TRIGRAM = """\
SELECT indexname FROM pg_indexes
 WHERE indexname IN %s
   AND indexdef NOT LIKE '%%gin_trgm_ops%%'
   AND schemaname = current_schema;
"""


class Partner(models.Model):
    _inherit = "res.partner"

    # Fields which should have been declared index="trigram"
    # These are the "_rec_names_search" fields + "name":
    # _rec_names_search = ['display_name', 'email', 'ref', 'vat', 'company_registry']

    name = fields.Char(index="trigram")
    display_name = fields.Char(index="trigram")
    email = fields.Char(index="trigram")
    ref = fields.Char(index="trigram")
    vat = fields.Char(index="trigram")
    company_registry = fields.Char(index="trigram")

    def init(self):
        # pylint: disable=missing-return
        super().init()
        if self.pool.has_trigram:
            tgm_indexes = tuple(
                f"{self._table}_{col}_index"
                for col in ["name"] + self._rec_names_search
            )
            self.env.cr.execute(QUERY_NOT_TRIGRAM, [tgm_indexes])
            for [index_name] in self.env.cr.fetchall():
                # Index has to be removed in order to be created with trigram later
                # Method self.pool.check_indexes(), during module installation/upgrade
                drop_index(self.env.cr, index_name, self._table)
