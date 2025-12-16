import json
import matplotlib.pyplot as plt

class SafetyAnalytics:
    def __init__(self, log_file="final_test_audit.log"):
        self.log_file = log_file

    def generate_safety_report(self):
        trust_scores = []
        outcomes = []
        
        with open(self.log_file, "r") as f:
            for line in f:
                data = json.loads(line)
                trust_scores.append(data['trust_score'])
                outcomes.append(data['outcome'])

        # Create the Visualization
        plt.figure(figsize=(10, 5))
        colors = ['green' if o == "APPROVED" else 'red' for o in outcomes]
        
        plt.scatter(range(len(trust_scores)), trust_scores, c=colors, s=100, alpha=0.6)
        plt.axhline(y=0.65, color='gray', linestyle='--', label='Safety Threshold')
        
        plt.title("PathX Safety Decision Distribution")
        plt.ylabel("System Trust Score")
        plt.xlabel("Mission Number")
        plt.grid(True, alpha=0.3)
        plt.show()
        
        print(f"✅ Report generated from {len(trust_scores)} missions.")
