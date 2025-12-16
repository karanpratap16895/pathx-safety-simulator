class DroneState:
    def __init__(self):
        self.gps_confidence = 1.0
        self.is_airborne = False
    def get_hardware_safety_score(self, wind):
        return 0.98 if wind < 35 else 0.7
