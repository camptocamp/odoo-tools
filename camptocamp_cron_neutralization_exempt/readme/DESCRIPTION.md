Adds a "Neutralization Exempt" flag on scheduled actions. Flagged crons stay active on
non-production environments after database neutralization, instead of staying disabled
until manually reactivated — a fix that wouldn't survive the next restore/neutralization
otherwise.
