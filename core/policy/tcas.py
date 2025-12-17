import time
import math

class TCASController:
    def __init__(self, grid_cell_id="ZONE_ALPHA"):
        self.grid_id = grid_cell_id
        self.max_capacity = 20  # Max drones allowed in this "Grid Cell"
        self.current_traffic = 0
        self.stats = {"autonomous_decisions": 0, "human_interventions": 0}
        self.doctrine = "TCAS RA overrides all mission intent. Priority: MED > EMER > COMM."

    def evaluate_grid_capacity(self):
        """Feature: Prevents congestion before it happens."""
        if self.current_traffic >= self.max_capacity:
            return False # Grid is "Full"
        return True

    def get_resolution_advisory(self, mission_profile, intruders, battery):
        """
        AI-driven conflict resolution for Drones & Future eVTOLs.
        Includes Dynamic Rerouting logic.
        """
        self.stats["autonomous_decisions"] += 1
        
        # 1. Performance Gate (Battery/Range)
        # Calculates if drone has 20% 'Safety Buffer' for return trip
        if battery < 20:
            return "RA_EMERGENCY_LANDING_IMMEDIATE"

        if not intruders:
            return "CLEAR_OF_CONFLICT"

        # 2. Conflict Arbitration
        critical = min(intruders, key=lambda x: x['dist'])
        
        # 3. Dynamic Rerouting (The Missing Logic)
        if critical['dist'] < 30:
            if mission_profile['priority'] == "MEDICAL":
                return "RA_MAINTAIN_COURSE_PRIORITY" # Medical stays on path
            else:
                # Commercial drone is told to reroute
                return "RA_REROUTE_TO_ALT_CORRIDOR_B"

        return "CLEAR_OF_CONFLICT"
