import json
from datetime import datetime

class BlackBoxLogger:
    def __init__(self, filename="flight_audit.log"):
        self.filename = filename

    def log_verdict(self, verdict, env_data, drone_data):
        """Saves a permanent record of a safety decision to a JSON-line file."""
        entry = {
            "timestamp": verdict.timestamp,
            "outcome": verdict.outcome,
            "policy_id": verdict.policy_id,
            "trust_score": verdict.trust,
            "reason": verdict.reason,
            "telemetry_snapshot": {
                "wind_speed": env_data.wind_speed,
                "propulsion_health": drone_data.health.get_aggregate_health()
            }
        }
        
        # We use 'a' for 'append' so we don't overwrite previous logs
        with open(self.filename, "a") as f:
            f.write(json.dumps(entry) + "\n")
        
        print(f"[SYSTEM] Legal audit trail updated: {self.filename}")
