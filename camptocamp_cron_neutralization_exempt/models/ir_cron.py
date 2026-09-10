# Copyright 2026 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class IrCron(models.Model):
    _inherit = "ir.cron"

    neutralization_exempt = fields.Boolean(
        string="Neutralization Exempt",
        help="If checked, this cron stays active after database neutralization.",
    )
