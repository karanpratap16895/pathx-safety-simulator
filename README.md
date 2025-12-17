> [!CAUTION]
> **IMPORTANT NOTICE: LEGAL & OPERATIONAL DISCLAIMER**
> 
> This repository contains **simulation and research code only.** It is **NOT** validated, certified, or approved for real-world flight or autonomous operations. 
> 
> Any operational use requires independent verification, certified hardware, and regulatory approval. Use of this code for operational systems is strictly prohibited. Regulatory engagement and certification compliance are required before any real-world application.

# PathX: Autonomous Safety Grid & Mission Orchestrator (v1.6.0)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

PathX is a **neutral safety grid** for autonomous aerial logistics. It acts as the "Air Traffic Control + Safety OS" layer that allows drones and eVTOLs from any manufacturer to fly safely, legally, and at scale.

## 🛡️ Safety Philosophy: The Autonomous Grid
The system operates on the principle of **Autonomous Refusal**. PathX implements a "Pessimistic Risk Model" to determine if a mission should proceed based on coupled environmental, hardware, and airspace stressors. 

### Key Pillars:
1. **AI-Driven Grid:** High-frequency collision avoidance and task assignment.
2. **Human-Monitored:** Strategic oversight with a formal "Authority Veto" interface.
3. **Hassle-Free Autonomy:** Seamless integration for OEMs via the PathX Safety API.

## 🛰️ Collision Avoidance (TCAS-inspired)
This module simulates TCAS-like collision avoidance logic adapted for unmanned systems. It is **NOT** an implementation of certified TCAS and is intended solely for safety research, simulation, and policy validation. It features:
* **Vertical Rate Envelopes:** Per-class performance limits (Light Utility vs. Emergency Med).
* **Predictive Trajectory Cones:** ML-based projections of future intruder positions.
* **Priority Arbitration:** Medical > Emergency > Disaster > Commercial.

## 🏗️ PathX Grid Architecture (v1.6.0)
The project follows a modular "Clean Architecture" design for forensic traceability:

```text
      [ AIR TRAFFIC ]          [ ENVIRONMENT ]          [ DRONE HARDWARE ]
       (Other Drones)            (Wind/Storms)            (Motor Health)
              \                       |                       /
      _________v______________________v______________________v__________
     |                                                                 |
     |              PATHX GRID ENGINE (Safety Layer)                   |
     |_________________________________________________________________|
     |                                                                 |
     |  1. Grid Capacity Management (Congestion Control)               |
     |  2. Dynamic Rerouting (Conflict Resolution)                     |
     |  3. Fault Containment Zones (Airspace Circuit Breaker)          |
     |_________________________________________________________________|
              /                       \
      _______v________         ________v_______
     |  PROJECT APEX  |       | AUTHORITY API  |
     | (Mission Layer)|       | (City Mode)    |
     |________________|       |________________|
              |                        |
     [ MISSION MANIFEST ] <---- [ FORENSIC LOG ]
