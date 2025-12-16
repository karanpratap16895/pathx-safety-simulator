from core.decision.verdict import PathXVerdict
def pathx_safety_engine(env, drone, system):
    system.update_recovery()
    trust = env.get_confidence() * drone.get_hardware_safety_score(env.wind_speed)
    trust *= (1.0 - (system.stress_level * 0.5))
    if env.wind_speed > 40:
        system.add_stress(0.4)
        return PathXVerdict("REFUSE", "Extreme Wind", trust, "POL_ENV_MAX")
    return PathXVerdict("APPROVED", "Nominal", trust, "POL_NOMINAL")
