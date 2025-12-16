# PathX: Autonomous Safety Validation Framework (v1.2.0)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

PathX is a high-fidelity safety simulation framework designed to validate autonomous decision-making under stress. It focuses on **Pre-Certification Auditing** by modeling the coupling between environmental hazards (high-velocity winds) and hardware degradation (propulsion failure).

## 🛡️ Safety Philosophy: Autonomous Interception
Unlike traditional flight controllers that prioritize mission completion, PathX prioritizes **Incident Prevention**. The engine evaluates a "Trust Score" to determine if a mission should be intercepted before a critical failure occurs.



## 🏗️ Technical Architecture
The system is built on a modular "Clean Architecture" for forensic traceability:
- `core/policy`: The v4.1 Decision Brain (Pessimistic Risk Model).
- `core/logging`: Forensic "Black Box" with automated Simulation Manifests.
- `core/state`: Coupled physics modeling for environment and hardware health.
- `core/engine`: High-volume batch processing and safety analytics.

## 📊 Validation Metrics
We measure system performance using aviation-grade KPIs:
* **Interception Rate:** Success in identifying and blocking unsafe flight states.
* **Critical Incident Rate:** Frequency of "Approved" flights that exceed safety thresholds (Target: 0%).
* **Forensic Auditability:** Every decision is logged with a unique manifest for post-mission review.

## 🚀 Quick Start (Validation Run)
Run the internal validation assessment directly in a portable Python environment:

```python
import subprocess, os
repo = "[https://github.com/karanpratap16895/pathx-safety-simulator.git](https://github.com/karanpratap16895/pathx-safety-simulator.git)"
if not os.path.exists("pathx-safety-simulator"):
    subprocess.run(["git", "clone", repo])
# See main.py for execution logic
