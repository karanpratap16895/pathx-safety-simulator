"""
PathX TCAS Module (Traffic Collision Avoidance System)
Standard: Based on RTCA DO-185B logic for Resolution Advisories (RA).
"""

class TCASController:
    def __init__(self, tau_threshold=15, dmod_m=20):
        """
        :param tau_threshold: Time to impact (seconds) that triggers an Advisory.
        :param dmod_m: Distance Modification (meters). Minimum safety bubble.
        """
        self.tau_threshold = tau_threshold
        self.dmod = dmod_m

    def calculate_tau(self, distance, closing_speed):
        """Calculates the time-to-collision constant."""
        if closing_speed <= 0:
            return float('inf')  # Targets are moving away
        return distance / closing_speed

    def get_resolution_advisory(self, intruder_dist, intruder_speed, rel_alt):
        """
        Determines the Resolution Advisory (RA).
        :param intruder_dist: Distance to intruder in meters.
        :param intruder_speed: Closing speed in m/s.
        :param rel_alt: Relative altitude (Positive = Intruder is above).
        """
        tau = self.calculate_tau(intruder_dist, intruder_speed)

        # 1. Check for immediate violation of the 'Safety Bubble' (DMOD)
        if intruder_dist < self.dmod:
            return "RA_IMMEDIATE_AVOIDANCE"

        # 2. Check for Tau violation (Time-based collision risk)
        if tau < self.tau_threshold:
            # If intruder is above, we advise descending. If below, we advise climbing.
            if rel_alt > 0:
                return "RA_DESCEND"
            else:
                return "RA_CLIMB"

        # 3. Warning phase
        if tau < (self.tau_threshold + 10):
            return "TA_TRAFFIC_ADVISORY"

        return "CLEAR_OF_CONFLICT"

    def process_safety_intercept(self, advisory):
        """Maps TCAS state to PathX Interception logic."""
        if "RA_" in advisory:
            return {
                "action": "INTERCEPT",
                "priority": "CRITICAL",
                "maneuver": advisory
            }
        return {"action": "PROCEED", "priority": "NOMINAL"}
