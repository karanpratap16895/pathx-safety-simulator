import time
import math

class TCASController:
    def __init__(self, grid_cell_id="URBAN_SECTOR_1"):
        self.grid_id = grid_cell_id
        self.max_capacity = 25  # Grid-level congestion control
        self.current_traffic = 12 
        self.fcz_active = False
        self.ai_confidence = 1.0
        self.precedence_doctrine = "TCAS RA overrides all policies except imminent ground impact."

    def evaluate_grid_capacity(self):
        """AI Check: Prevents congestion before takeoff."""
        return self.current_traffic < self.max_capacity

    def get_resolution_advisory(self, mission, intruders, battery, external_override=False):
        """
        AI Separation Engine with Human Authority Interface.
        """
        # 1. External Authority Veto (CAA/City Mode)
        if external_override:
            return "RA_AUTHORITY_MANDATED_GROUNDING"

        # 2. Performance & Liability Guard
        if battery < 20:
            return "RA_EMERGENCY_LANDING_LOW_POWER"

        if not intruders:
            return "CLEAR_OF_CONFLICT"

        # 3. Conflict Arbitration (Medical > Commercial)
        critical = min(intruders, key=lambda x: x['dist'])
        
        if critical['dist'] < 30:
            if mission['priority'] == "MEDICAL":
                return "RA_MAINTAIN_COURSE_PRIORITY"
            else:
                # Dynamic Rerouting Logic
                return "RA_REROUTE_TO_ALT_CORRIDOR"

        return "CLEAR_OF_CONFLICT"
