from core.state.environment import EnvironmentState
from core.state.drone import DroneState
from core.state.system import SystemState
from core.policy.engine_v4_1 import pathx_safety_engine
from core.logging.blackbox import BlackBoxLogger

def run_audited_sim():
    # Setup
    env = EnvironmentState(wind=45) # Trigger a refusal
    drone = DroneState()
    system = SystemState()
    logger = BlackBoxLogger() # Initialize recorder

    # Run Engine
    verdict = pathx_safety_engine(env, drone, system, logger=logger)
    
    print(f"\nFinal Verdict: {verdict.outcome}")
    print("Check 'flight_audit.log' for the JSON audit trail.")

if __name__ == "__main__":
    run_audited_sim()
