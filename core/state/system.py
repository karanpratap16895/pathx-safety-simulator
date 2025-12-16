import time
class SystemState:
    def __init__(self):
        self.stress_level = 0.0
        self.last_update = time.time()
    def update_recovery(self):
        now = time.time()
        self.stress_level = max(0.0, self.stress_level - ((now - self.last_update)/600))
        self.last_update = now
    def add_stress(self, amount=0.3):
        self.stress_level = min(1.0, self.stress_level + amount)
