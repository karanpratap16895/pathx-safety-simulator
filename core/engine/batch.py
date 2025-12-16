import random
from core.state.environment import EnvironmentState
from core.state.drone import DroneState
from core.state.system import SystemState
from core.policy.engine_v4_1 import pathx_safety_engine

class BatchSimulator:
    def __init__(self, logger=None):
        self.logger = logger
        # Use professional metrics: APPROVED (Nominal) and SAFETY_INTERCEPT (Success)
        self.metrics = {"APPROVED": 0, "SAFETY_INTERCEPT": 0}

    def run_stress_test(self, iterations=50):
        system = SystemState()
        
        for i in range(iterations):
            # Generate random conditions
            wind = random.uniform(0, 55)
            env = EnvironmentState(wind=wind)
            drone = DroneState()
            
            # 15% chance of motor damage
            if random.random() < 0.15:
                drone.health.inject_motor_failure(random.randint(0,3), 0.4)
            
            # Get the verdict from the brain
            verdict = pathx_safety_engine(env, drone, system, logger=self.logger)
            
            # Map the verdict to professional safety metrics
            if verdict.outcome == "REFUSE":
                # A 'Refusal' is a successful safety interception
                self.metrics["SAFETY_INTERCEPT"] += 1
            else:
                self.metrics["APPROVED"] += 1
            
        return self.metrics
