class HardwareHealth:
    def __init__(self):
        # 1.0 is healthy, 0.0 is total failure
        self.motor_efficiency = [1.0, 1.0, 1.0, 1.0] 
        self.structural_integrity = 1.0

    def inject_motor_failure(self, motor_index, loss_percentage):
        """Simulates a bird strike or mechanical failure."""
        self.motor_efficiency[motor_index] -= loss_percentage
        print(f"[!] INJECTED: Motor {motor_index} failed by {loss_percentage*100}%")

    def get_aggregate_health(self):
        """Returns the average health of all propulsion units."""
        return sum(self.motor_efficiency) / len(self.motor_efficiency)
