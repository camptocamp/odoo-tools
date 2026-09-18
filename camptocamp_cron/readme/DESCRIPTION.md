Adds a "Keep Active" flag on scheduled actions. Flagged crons are automatically
re-activated whenever they are found inactive — including after database neutralization
on non-production environments — instead of staying disabled until manually reactivated,
a fix that wouldn't survive the next restore/neutralization otherwise.
