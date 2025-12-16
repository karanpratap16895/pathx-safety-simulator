import json
import random
import sys
import os
from datetime import datetime

# --- SAFETY CATCH ---
# This line tells the computer to look in the current folder for your 'core' files
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from core.policy.tcas import TCASController
except ImportError:
    print("ERROR: Could not find tcas.py. Make sure core/policy/tcas.py exists!")
    exit(1)

def run_safety_assessment():
    tcas_engine = TCASController(tau_threshold=15)
    
    # NEW: Multi-Intruder Data (Missing Feature #2)
    intruder_list = [
        {"dist": 45.0, "speed": 6.0, "rel_alt": 5.0},   # Intruder A
        {"dist": 80.0, "speed": 2.0, "rel_alt": -2.0}  # Intruder B
    ]

    # Precedence Doctrine (Missing Feature #4)
    # TCAS RA overrides all non-structural policies except imminent ground impact.
    
    advisory = tcas_engine.get_resolution_advisory(intruder_list)

    # Missing Feature #5: Audit Trace Linkage
    tcas_audit_data = {
        "advisory": advisory,
        "primary_threat_tau": 45.0/6.0, # distance/speed
        "precedence_rule": "TCAS_OVERRIDE_ACTIVE" if "RA_" in advisory else "STANDARD"
    }

    # Decide
    if "RA_" in advisory:
        verdict = "REFUSE"
        reason = f"TCAS OVERRIDE: {advisory}"
    elif random.uniform(0, 60) > 45: # Example weather check
        verdict = "REFUSE"
        reason = "WEATHER_LIMIT"
    else:
        verdict = "APPROVE"
        reason = "NOMINAL"

    # Print for Investor Audit
    print(f"VERDICT: {verdict} | REASON: {reason}")
    print(f"AUDIT TRACE: {json.dumps(tcas_audit_data, indent=2)}")
    
    # 2. INPUTS: Simulating random real-world conditions
    wind_speed = random.uniform(0, 60)         # mph
    motor_health = random.uniform(0.5, 1.0)    # 1.0 is perfect health
    
    # TCAS Inputs (Simulating a nearby 'Intruder' drone)
    intruder_dist = random.uniform(10, 100)    # How many meters away?
    closing_speed = random.uniform(0, 15)      # How fast is it coming at us?
    rel_alt = random.uniform(-10, 10)          # Is it above (+) or below (-) us?

    # 3. EVALUATION: The 'Safety Brain' makes a decision
    # STEP A: Check for Collision (This is the most important)
    advisory = tcas_engine.get_resolution_advisory(intruder_dist, closing_speed, rel_alt)
    
    # If the advisory starts with "RA", it's a 'Resolution Advisory' (Must Stop)
    if "RA_" in advisory:
        verdict = "REFUSE"
        reason = f"CRITICAL AIRSPACE CONFLICT: {advisory}"
    
    # STEP B: If air is clear, check weather and hardware
    elif wind_speed > 45 or motor_health < 0.7:
        verdict = "REFUSE"
        reason = "ENVIRONMENTAL/HARDWARE RISK"
    
    # STEP C: If everything is safe
    else:
        verdict = "APPROVE"
        reason = "NOMINAL CONDITIONS"

    # 4. FORENSIC LOG: Create the digital "Black Box" record
    manifest = {
        "timestamp": datetime.now().isoformat(),
        "engine_version": "1.2.1",
        "verdict": verdict,
        "reason": reason,
        "telemetry_snapshot": {
            "wind_mph": round(wind_speed, 2),
            "motor_index": round(motor_health, 2),
            "tcas_status": advisory,
            "intruder_distance_m": round(intruder_dist, 2)
        }
    }

    # Print the result to the screen
    print(f"\n--- PATHX SAFETY CHECK: {verdict} ---")
    print(f"DECISION REASON: {reason}")
    print("\n--- FORENSIC MANIFEST DATA ---")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    run_safety_assessment()
