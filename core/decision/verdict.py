from datetime import datetime
class PathXVerdict:
    def __init__(self, outcome, reason, trust, policy_id):
        self.outcome = outcome
        self.reason = reason
        self.trust = round(trust, 4)
        self.policy_id = policy_id
        self.timestamp = datetime.now().isoformat()
