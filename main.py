from core.state.environment import EnvironmentState
from core.state.drone import DroneState
from core.state.system import SystemState
from core.policy.engine_v4_1 import pathx_safety_engine

def run_stress_test():
    # 1. Setup the scenario
    # Even with LOW wind (20kt), a broken motor should trigger a refusal.
    env = EnvironmentState(wind=20) 
    drone = DroneState()
    system = SystemState()

    print("--- PHASE 1: PRE-FAILURE (NOMINAL) ---")
    verdict_1 = pathx_safety_engine(env, drone, system)
    print(f"VERDICT: {verdict_1.outcome} | TRUST: {verdict_1.trust}")

    print("\n--- PHASE 2: INJECTING MOTOR FAILURE ---")
    # We simulate Motor #1 losing 60% of its power (0.6 loss)
    drone.health.inject_motor_failure(motor_index=1, loss_percentage=0.6)
    
    # Execute the safety engine again
    verdict_2 = pathx_safety_engine(env, drone, system)
    
    print(f"VERDICT: {verdict_2.outcome} | REASON: {verdict_2.reason}")
    print(f"TRUST SCORE: {verdict_2.trust}")
    
    if verdict_2.outcome == "REFUSE":
        print("\n[SUCCESS] The engine successfully detected the hardware failure.")

if __name__ == "__main__":
    run_stress_test()
