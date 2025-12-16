"""
PathX TCAS Module v1.2.3 (Performance-Aware)
Includes Memory, Multi-Intruder Arbitration, and Battery Feasibility Gates.
"""
import time

class TCASController:
    def __init__(self, tau_threshold=15, dmod_m=20):
        self.tau_threshold = tau_threshold
        self.dmod = dmod_m
        self.last_advisory = "CLEAR_OF_CONFLICT"
        self.last_ra_time = 0
        self.min_ra_duration = 5 
        # Feature #4: Explicit Doctrine
        self.precedence_doctrine = "TCAS RA overrides all policies except imminent ground impact."

    def calculate_tau(self, distance, closing_speed):
        if closing_speed <= 0: return float('inf')
        return distance / closing_speed

    def get_resolution_advisory(self, intruders, battery_level, can_climb_fast):
        """
        NEW: Feature #3 - Feasibility Gate
        Checks if the drone has the power/capability to climb.
        """
        now = time.time()
        if not intruders:
            return "CLEAR_OF_CONFLICT"

        # Feature #2: Multi-Intruder Arbitration
        critical_intruder = min(intruders, key=lambda x: self.calculate_tau(x['dist'], x['speed']))
        tau = self.calculate_tau(critical_intruder['dist'], critical_intruder['speed'])
        rel_alt = critical_intruder['rel_alt']

        # Feature #1: Statefulness (Memory)
        if (now - self.last_ra_time) < self.min_ra_duration and "RA_" in self.last_advisory:
            return self.last_advisory

        # Feature #3 Logic: Performance Check
        potential_advisory = "CLEAR_OF_CONFLICT"
        if tau < self.tau_threshold:
            if rel_alt > 0:
                potential_advisory = "RA_DESCEND"
            else:
                # If battery is < 15% or motors are stressed, we cannot climb safely
                if battery_level < 15 or not can_climb_fast:
                    potential_advisory = "RA_IMMEDIATE_AVOIDANCE" # Emergency lateral break
                else:
                    potential_advisory = "RA_CLIMB"

        self.last_advisory = potential_advisory
        if "RA_" in potential_advisory: self.last_ra_time = now
        return potential_advisory
