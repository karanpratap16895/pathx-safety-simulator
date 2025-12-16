# PathX Safety Doctrine
## The Pessimistic Risk Model
PathX operates on the principle of **Autonomous Interception**. 

### 1. Risk Coupling
We assume that environmental stressors (wind) and hardware degradation (motor failure) are not independent. High wind increases the load on a failing motor, accelerating the risk of a critical incident.

### 2. Decision Thresholds
* **Trust Score > 0.80:** Nominal Flight.
* **Trust Score 0.65 - 0.80:** Cautionary State (Requires monitoring).
* **Trust Score < 0.65:** Safety Interception (Mission Abort).
