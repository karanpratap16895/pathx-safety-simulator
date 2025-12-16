from core.decision.verdict import PathXVerdict

def pathx_safety_engine(env, drone, system, logger=None):
    system.update_recovery()
    
    # Calculate Trust with Hardware Health coupling
    trust = env.get_confidence() * drone.get_hardware_safety_score(env.wind_speed)
    trust *= (1.0 - (system.stress_level * 0.5))

    # Determine Verdict
    if env.wind_speed > 40:
        system.add_stress(0.4)
        v = PathXVerdict("REFUSE", "Extreme Wind Velocity", trust, "POL_ENV_001")
    elif trust < 0.65:
        system.add_stress(0.2)
        v = PathXVerdict("REFUSE", "Confidence Collapse", trust, "POL_SYS_999")
    else:
        v = PathXVerdict("APPROVED", "Nominal", trust, "POL_GEN_001")

    # If a logger is active, record the decision permanently
    if logger:
        logger.log_verdict(v, env, drone)
        
    return v
