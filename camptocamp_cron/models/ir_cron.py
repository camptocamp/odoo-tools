# Copyright 2026 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class IrCron(models.Model):
    _inherit = "ir.cron"

    keep_active = fields.Boolean(
        string="Keep Active",
        help="If checked, this cron is automatically re-activated whenever it is"
        " found inactive (e.g. after database neutralization), independently of"
        " why it was deactivated.",
    )
