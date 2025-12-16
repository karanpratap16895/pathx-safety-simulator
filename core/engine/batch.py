import random
from core.state.environment import EnvironmentState
from core.state.drone import DroneState
from core.state.system import SystemState
from core.policy.engine_v4_1 import pathx_safety_engine

class BatchSimulator:
    def __init__(self, logger=None):
        self.logger = logger
        self.stats = {"APPROVED": 0, "REFUSE": 0}

    def run_stress_test(self, iterations=50):
        print(f"--- Launching {iterations} Simulated Missions ---")
        system = SystemState()
        
        for i in range(iterations):
            # Randomize wind between 0 and 55 knots
            wind = random.uniform(0, 55)
            env = EnvironmentState(wind=wind)
            drone = DroneState()
            
            # 15% chance of a random hardware glitch mid-simulation
            if random.random() < 0.15:
                drone.health.inject_motor_failure(random.randint(0,3), 0.4)
            
            verdict = pathx_safety_engine(env, drone, system, logger=self.logger)
            self.stats[verdict.outcome] = self.stats.get(verdict.outcome, 0) + 1
            
        return self.stats
