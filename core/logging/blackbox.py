import json
from datetime import datetime

class BlackBoxLogger:
    def __init__(self, filename="validation_audit.log"):
        self.filename = filename

    def write_manifest(self, manifest_data):
        """Writes the simulation metadata at the start of the log."""
        header = {
            "log_type": "SIMULATION_MANIFEST",
            "timestamp": datetime.now().isoformat(),
            "metadata": manifest_data
        }
        with open(self.filename, "a") as f:
            f.write(json.dumps(header) + "\n---\n")

    def log_verdict(self, verdict, env_data, drone_data):
        """Saves a permanent record of a safety decision."""
        entry = {
            "timestamp": verdict.timestamp,
            "outcome": verdict.outcome,
            "policy_id": verdict.policy_id,
            "trust_score": verdict.trust,
            "reason": verdict.reason,
            "telemetry": {
                "wind": env_data.wind_speed,
                "propulsion_health": drone_data.health.get_aggregate_health()
            }
        }
        with open(self.filename, "a") as f:
            f.write(json.dumps(entry) + "\n")
