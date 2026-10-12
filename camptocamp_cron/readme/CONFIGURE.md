This module only provides the field; it has no effect on its own.

Re-activation of flagged crons is performed by the `004_restore_keep_active_crons`
`start-entrypoint.d` script of the
[docker-odoo-project](https://github.com/camptocamp/docker-odoo-project) base image,
which re-enables them on every start, skipped on production. Set
`RESTORE_KEEP_ACTIVE_CRONS=False` to disable it.
