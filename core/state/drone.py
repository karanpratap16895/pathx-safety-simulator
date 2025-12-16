from core.state.hardware_health import HardwareHealth

class DroneState:
    def __init__(self):
        self.gps_confidence = 1.0
        self.is_airborne = False
        self.health = HardwareHealth() # New: Link health to drone

    def get_hardware_safety_score(self, wind):
        # Combine GPS trust with physical motor health
        propulsion_score = self.health.get_aggregate_health()
        
        # If a motor is failing, wind becomes 2x more dangerous
        wind_vulnerability = 1.0 if propulsion_score > 0.9 else 2.0
        
        if wind * wind_vulnerability > 35:
            return 0.5 * propulsion_score
            
        return self.gps_confidence * propulsion_score
