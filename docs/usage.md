# Technical Usage Guide
## Configuration
To modify simulation parameters, navigate to `core/state/environment.py`. You can adjust the `wind_speed` variable to simulate specific storm categories.

## Interpreting Logs
The `internal_validation_audit.log` is a JSON-line formatted file. Every entry includes a `telemetry` block and a `trust_score` which was used by the engine to reach its verdict.
