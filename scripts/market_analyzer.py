import requests
import json
from datetime import datetime

class MarketAnalyzer:
    def __init__(self):
        self.github_trending = "https://api.github.com/search/repositories"
        
    def get_github_trends(self):
        params = {
            'q': 'created:>2024-01-01',
            'sort': 'stars',
            'order': 'desc',
            'per_page': 10
        }
        
        try:
            response = requests.get(self.github_trending, params=params)
            trending_repos = response.json().get('items', [])
            
            trends = {
                "languages": self.extract_languages(trending_repos),
                "topics": self.extract_topics(trending_repos),
                "update_date": datetime.now().isoformat()
            }
            
            with open('market_trends.json', 'w') as f:
                json.dump(trends, f, indent=2)
                
            return trends
            
        except Exception as e:
            print(f"Error fetching trends: {e}")
            return {}
    
    def extract_languages(self, repos):
        languages = {}
        for repo in repos:
            lang = repo.get('language')
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
        return dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))
    
    def extract_topics(self, repos):
        topics = {}
        for repo in repos:
            repo_topics = repo.get('topics', [])
            for topic in repo_topics:
                topics[topic] = topics.get(topic, 0) + 1
        return dict(sorted(topics.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    analyzer = MarketAnalyzer()
    trends = analyzer.get_github_trends()
    print("Market analysis completed!")
