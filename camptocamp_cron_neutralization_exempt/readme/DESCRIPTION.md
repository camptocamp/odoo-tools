Adds a "Neutralization Exempt" flag on scheduled actions
(`Settings > Technical > Scheduled Actions`). Crons flagged this way are re-enabled
after the database neutralization that runs on non-production environments, instead of
staying disabled until someone re-activates them manually from the UI (a change that is
otherwise reset on the next container restart).

This module only provides the field. The re-activation itself is performed by a
`start-entrypoint.d` script provided by odoo-template, which runs after neutralization
on every container boot.
