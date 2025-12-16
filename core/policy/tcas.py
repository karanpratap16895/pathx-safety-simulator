"""
PathX TCAS Module v1.2.2 (Stateful)
Includes Memory, Hysteresis, and Multi-Intruder Arbitration.
"""
import time

class TCASController:
    def __init__(self, tau_threshold=15, dmod_m=20):
        self.tau_threshold = tau_threshold
        self.dmod = dmod_m
        
        # --- NEW: Statefulness (Memory) ---
        self.last_advisory = "CLEAR_OF_CONFLICT"
        self.last_ra_time = 0
        self.min_ra_duration = 5  # Seconds an RA must stay active
        self.precedence_doctrine = "TCAS RA overrides all policies except imminent ground impact."

    def calculate_tau(self, distance, closing_speed):
        if closing_speed <= 0:
            return float('inf')
        return distance / closing_speed

    def get_resolution_advisory(self, intruders):
        """
        NEW: Accepts a LIST of intruders (Multi-intruder arbitration)
        Each intruder = {"dist": x, "speed": y, "rel_alt": z}
        """
        now = time.time()

        # 1. Multi-Intruder Arbitration: Find the most critical threat
        if not intruders:
            self.last_advisory = "CLEAR_OF_CONFLICT"
            return self.last_advisory

        # Rank by lowest Tau (time to impact)
        critical_intruder = min(intruders, key=lambda x: self.calculate_tau(x['dist'], x['speed']))
        
        dist = critical_intruder['dist']
        speed = critical_intruder['speed']
        rel_alt = critical_intruder['rel_alt']
        tau = self.calculate_tau(dist, speed)

        # 2. Memory/Hysteresis Logic: Don't flip-flop too fast
        if (now - self.last_ra_time) < self.min_ra_duration and "RA_" in self.last_advisory:
            return self.last_advisory

        # 3. Decision Logic
        new_advisory = "CLEAR_OF_CONFLICT"
        if dist < self.dmod:
            new_advisory = "RA_IMMEDIATE_AVOIDANCE"
        elif tau < self.tau_threshold:
            new_advisory = "RA_DESCEND" if rel_alt > 0 else "RA_CLIMB"
        elif tau < (self.tau_threshold + 10):
            new_advisory = "TA_TRAFFIC_ADVISORY"

        # Update Memory
        if "RA_" in new_advisory:
            self.last_ra_time = now
        
        self.last_advisory = new_advisory
        return new_advisory
