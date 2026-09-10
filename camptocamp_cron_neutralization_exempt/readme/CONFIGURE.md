This module only provides the field; it has no effect on its own.

Re-activation of flagged crons is performed by a paired `start-entrypoint.d` script from
[odoo-template](https://github.com/camptocamp/odoo-template), which unconditionally
re-enables them after neutralization. A project must pull in that script for the flag to
have any effect.
