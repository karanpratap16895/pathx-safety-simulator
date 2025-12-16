from core.state.environment import EnvironmentState
from core.state.drone import DroneState
from core.state.system import SystemState
from core.policy.engine_v4_1 import pathx_safety_engine

def run():
    env = EnvironmentState(wind=45)
    drone = DroneState()
    system = SystemState()
    verdict = pathx_safety_engine(env, drone, system)
    print(f"VERDICT: {verdict.outcome} | REASON: {verdict.reason}")

if __name__ == "__main__":
    run()
