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
    # 1. SETUP: Initialize the TCAS Engine
    tcas_engine = TCASController(tau_threshold=15)
    
    # 2. INPUTS: Simulating System State & Environment
    battery_pct = random.uniform(5, 100)       # Feature #3: Battery State
    motor_power_ready = True                   # Feature #3: Performance Gate
    wind_speed = random.uniform(0, 60)         # mph
    motor_health = random.uniform(0.5, 1.0)    # 1.0 is perfect
    
    # Feature #2: Multi-Intruder List (Simulating 3 nearby drones)
    intruder_list = [
        {"dist": random.uniform(30, 100), "speed": random.uniform(1, 10), "rel_alt": random.uniform(-5, 5)},
        {"dist": 35.0, "speed": 8.0, "rel_alt": -2.0}, # This is a critical threat
        {"dist": 150.0, "speed": 2.0, "rel_alt": 10.0}
    ]

    # 3. EVALUATION: The 'Safety Brain' makes a decision
    # STEP A: Check for Collision (TCAS check comes first)
    # We pass the list, the battery, and the motor status
    advisory = tcas_engine.get_resolution_advisory(
        intruder_list, 
        battery_pct, 
        motor_power_ready
    )
    
    # Feature #4: Precedence Doctrine 
    # "TCAS Resolution Advisories override all non-structural policies"
    if "RA_" in advisory:
        verdict = "REFUSE"
        reason = f"TCAS OVERRIDE: {advisory}"
        precedence = "CRITICAL_TCAS_CONTROL"
    
    # STEP B: If no collision risk, check weather and hardware
    elif wind_speed > 45 or motor_health < 0.7:
        verdict = "REFUSE"
        reason = "ENVIRONMENTAL/HARDWARE RISK"
        precedence = "STANDARD_SAFETY_LIMIT"
    
    # STEP C: If everything is safe
    else:
        verdict = "APPROVE"
        reason = "NOMINAL CONDITIONS"
        precedence = "STANDARD_SAFETY_LIMIT"

    # 4. FORENSIC LOG: Feature #5 (Audit Trace Linkage)
    manifest = {
        "timestamp": datetime.now().isoformat(),
        "engine_version": "1.2.3",
        "verdict": verdict,
        "reason": reason,
        "precedence_doctrine": precedence,
        "telemetry_snapshot": {
            "battery_level": round(battery_pct, 2),
            "wind_mph": round(wind_speed, 2),
            "motor_index": round(motor_health, 2),
            "tcas_status": advisory,
            "intruder_count": len(intruder_list)
        }
    }

    # Print the result to the screen for the Auditor/Reviewer
    print(f"\n--- PATHX SAFETY CHECK: {verdict} ---")
    print(f"DECISION REASON: {reason}")
    print(f"DOCTRINE: {precedence}")
    
    # Visual alert for the specific "Battery" issue the reviewer mentioned
    if battery_pct < 15 and advisory == "RA_IMMEDIATE_AVOIDANCE":
        print("!!! ALERT: LOW BATTERY DETECTED. VERTICAL MANEUVER GATED. !!!")

    print("\n--- FORENSIC MANIFEST DATA ---")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    run_safety_assessment()
