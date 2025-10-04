import json
from datetime import datetime

class CommunityMarketplace:
    def __init__(self):
        self.plugins = []
        self.themes = []
        self.templates = []
        self.transactions = []
    
    def submit_plugin(self, plugin_data):
        plugin = {
            "id": f"plugin_{len(self.plugins) + 1}",
            "name": plugin_data["name"],
            "developer": plugin_data["developer"],
            "description": plugin_data["description"],
            "category": plugin_data.get("category", "utility"),
            "price": plugin_data.get("price", 0),
            "version": "1.0.0",
            "compatibility": plugin_data.get("compatibility", ["all"]),
            "downloads": 0,
            "rating": 0,
            "reviews": [],
            "status": "pending",
            "submitted_at": datetime.now().isoformat()
        }
        
        self.plugins.append(plugin)
        return plugin
    
    def approve_plugin(self, plugin_id):
        plugin = self.get_plugin(plugin_id)
        if plugin:
            plugin["status"] = "approved"
            plugin["approved_at"] = datetime.now().isoformat()
            return plugin
        return None
    
    def get_plugin(self, plugin_id):
        for plugin in self.plugins:
            if plugin["id"] == plugin_id:
                return plugin
        return None
    
    def download_plugin(self, plugin_id, user_id):
        plugin = self.get_plugin(plugin_id)
        if plugin and plugin["status"] == "approved":
            plugin["downloads"] += 1
            
            transaction = {
                "transaction_id": f"tx_{len(self.transactions) + 1}",
                "plugin_id": plugin_id,
                "user_id": user_id,
                "amount": plugin["price"],
                "timestamp": datetime.now().isoformat(),
                "type": "download"
            }
            
            self.transactions.append(transaction)
            return plugin
        
        return None
    
    def add_review(self, plugin_id, review_data):
        plugin = self.get_plugin(plugin_id)
        if plugin:
            review = {
                "user": review_data["user"],
                "rating": review_data["rating"],
                "comment": review_data.get("comment", ""),
                "timestamp": datetime.now().isoformat()
            }
            
            plugin["reviews"].append(review)
            
            # Update average rating
            if plugin["reviews"]:
                total_rating = sum(r["rating"] for r in plugin["reviews"])
                plugin["rating"] = total_rating / len(plugin["reviews"])
            
            return review
        
        return None
    
    def submit_theme(self, theme_data):
        theme = {
            "id": f"theme_{len(self.themes) + 1}",
            "name": theme_data["name"],
            "developer": theme_data["developer"],
            "description": theme_data["description"],
            "price": theme_data.get("price", 0),
            "downloads": 0,
            "status": "pending",
            "submitted_at": datetime.now().isoformat()
        }
        
        self.themes.append(theme)
        return theme
    
    def get_marketplace_stats(self):
        total_plugins = len(self.plugins)
        approved_plugins = len([p for p in self.plugins if p["status"] == "approved"])
        total_downloads = sum(p["downloads"] for p in self.plugins)
        total_revenue = sum(t["amount"] for t in self.transactions)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_plugins": total_plugins,
            "approved_plugins": approved_plugins,
            "total_themes": len(self.themes),
            "total_downloads": total_downloads,
            "total_revenue": total_revenue,
            "active_developers": len(set(p["developer"] for p in self.plugins)),
            "marketplace_health": self.assess_marketplace_health(total_plugins, total_downloads)
        }
    
    def assess_marketplace_health(self, total_plugins, total_downloads):
        if total_plugins >= 10 and total_downloads >= 100:
            return "thriving"
        elif total_plugins >= 5 and total_downloads >= 25:
            return "growing"
        elif total_plugins >= 1:
            return "emerging"
        else:
            return "developing"
    
    def generate_marketplace_report(self):
        stats = self.get_marketplace_stats()
        
        report = {
            "marketplace_overview": stats,
            "top_plugins": sorted(self.plugins, key=lambda x: x["downloads"], reverse=True)[:5],
            "recent_submissions": self.plugins[-5:] if self.plugins else [],
            "revenue_analytics": self.get_revenue_analytics(),
            "growth_recommendations": self.generate_growth_recommendations(stats)
        }
        
        with open('marketplace_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        return report
    
    def get_revenue_analytics(self):
        paid_plugins = [p for p in self.plugins if p["price"] > 0]
        free_plugins = [p for p in self.plugins if p["price"] == 0]
        
        return {
            "total_paid_plugins": len(paid_plugins),
            "total_free_plugins": len(free_plugins),
            "conversion_rate": len(paid_plugins) / len(self.plugins) if self.plugins else 0,
            "average_price": sum(p["price"] for p in paid_plugins) / len(paid_plugins) if paid_plugins else 0
        }
    
    def generate_growth_recommendations(self, stats):
        recommendations = []
        
        if stats["total_plugins"] < 10:
            recommendations.append("Launch developer incentive program")
        
        if stats["total_downloads"] < 50:
            recommendations.append("Promote marketplace to community")
        
        if stats["active_developers"] < 5:
            recommendations.append("Create developer documentation and SDK")
        
        recommendations.extend([
            "Implement plugin categories and tags",
            "Add plugin versioning and update system",
            "Create featured plugins section",
            "Add social sharing for plugins"
        ])
        
        return recommendations

marketplace = CommunityMarketplace()
