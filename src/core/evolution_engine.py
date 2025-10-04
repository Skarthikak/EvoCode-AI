import json
import requests
from datetime import datetime, timedelta

class EvolutionEngine:
    def __init__(self):
        self.feedback_data = []
        self.market_data = []
        self.evolution_history = []
        
    def collect_evolution_data(self):
        data = {
            "feedback": self.get_recent_feedback(),
            "market_trends": self.get_market_trends(),
            "github_activity": self.get_github_activity(),
            "competitor_analysis": self.analyze_competitors(),
            "timestamp": datetime.now().isoformat()
        }
        return data
    
    def get_recent_feedback(self):
        return {
            "positive": 85,
            "negative": 15,
            "feature_requests": ["better Python support", "VS Code integration"],
            "bug_reports": ["slow performance", "UI issues"]
        }
    
    def analyze_competitors(self):
        competitors = {
            "github_copilot": ["AI completions", "multi-language"],
            "vscode": ["extensions", "debugging"],
            "replit": ["cloud IDE", "collaboration"]
        }
        
        our_features = ["self_evolution", "community_driven", "github_native"]
        gaps = self.identify_feature_gaps(our_features, competitors)
        
        return {
            "competitors": competitors,
            "our_advantages": our_features,
            "feature_gaps": gaps,
            "recommendations": self.generate_recommendations(gaps)
        }
    
    def identify_feature_gaps(self, our_features, competitors):
        all_competitor_features = set()
        for features in competitors.values():
            all_competitor_features.update(features)
            
        our_feature_set = set(our_features)
        return list(all_competitor_features - our_feature_set)
    
    def generate_recommendations(self, gaps):
        recommendations = []
        
        for gap in gaps:
            if gap in ["debugging", "collaboration"]:
                recommendations.append({
                    "feature": gap,
                    "priority": "high",
                    "impact": "competitive_advantage",
                    "effort": "medium"
                })
        
        return recommendations
    
    def make_evolution_decision(self):
        data = self.collect_evolution_data()
        recommendations = data["competitor_analysis"]["recommendations"]
        
        high_priority = [r for r in recommendations if r["priority"] == "high"]
        
        evolution_plan = {
            "timestamp": datetime.now().isoformat(),
            "decisions": high_priority[:2],
            "rationale": "Market competition and user feedback",
            "expected_impact": "Increased market competitiveness"
        }
        
        self.evolution_history.append(evolution_plan)
        self.save_evolution_plan(evolution_plan)
        
        return evolution_plan
    
    def save_evolution_plan(self, plan):
        print(f"Evolution plan saved: {plan}")
        
    def generate_evolution_report(self):
        plan = self.make_evolution_decision()
        
        report = f"""
# Weekly Evolution Report - {datetime.now().strftime('%Y-%m-%d')}

## Decisions Made
{json.dumps(plan['decisions'], indent=2)}

## Rationale
{plan['rationale']}

## Expected Impact
{plan['expected_impact']}

## Next Steps
1. Implement selected features
2. Community review
3. Integration testing
"""
        return report

evolution_engine = EvolutionEngine()
