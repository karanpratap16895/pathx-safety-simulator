import time
class EnvironmentState:
    def __init__(self, wind=10):
        self.wind_speed = wind
        self.last_update = time.time()
    def get_confidence(self):
        age = time.time() - self.last_update
        return 0.95 if age < 30 else 0.5
