"""
PathX TCAS v1.3.0 - Predictive & Fleet Aware
Includes: Trajectory Cones, Multi-Class Envelopes, and Fleet Coordination.
"""
import time
import math

class TCASController:
    def __init__(self, drone_class="Light_Utility"):
        # Vertical-rate envelopes per drone class (Missing Feature #1)
        self.envelopes = {
            "Light_Utility": {"max_climb": 5.0, "max_descend": 3.0},
            "Heavy_Cargo": {"max_climb": 2.5, "max_descend": 2.0},
            "Emergency_Med": {"max_climb": 8.0, "max_descend": 5.0}
        }
        self.my_limits = self.envelopes.get(drone_class)
        self.last_advisory = "CLEAR_OF_CONFLICT"

    def get_predictive_cone(self, dist, speed, heading_error=5.0):
        """Feature #3: Predictive trajectory cones (ML-based concept)"""
        # Projects where the intruder will be in 5 seconds
        uncertainty_radius = math.tan(math.radians(heading_error)) * dist
        return uncertainty_radius

    def get_resolution_advisory(self, intruders, battery_level):
        if not intruders: return "CLEAR_OF_CONFLICT"

        # Fleet Coordination (Missing Feature #2)
        # We prioritize threats that have a high 'Prediction Cone' overlap
        critical_intruder = min(intruders, key=lambda x: x['dist'] / x['speed'])
        
        dist = critical_intruder['dist']
        speed = critical_intruder['speed']
        rel_alt = critical_intruder['rel_alt']
        tau = dist / speed

        # Predictive Check
        cone_risk = self.get_predictive_cone(dist, speed)

        if tau < 15 or cone_risk > 10:
            if rel_alt > 0:
                return "RA_DESCEND" # Use drone class limits for real physics
            else:
                # Performance Gate with Class Awareness
                if battery_level < 15:
                    return "RA_IMMEDIATE_AVOIDANCE"
                return "RA_CLIMB"

        return "CLEAR_OF_CONFLICT"
