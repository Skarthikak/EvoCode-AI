<<<<<<< HEAD
import json
from datetime import datetime

class CommunityMarketplace:
    def __init__(self):
        self.plugins = []
        self.themes = []
        self.templates = []
        self.transactions = []
=======
class CommunityMarketplace:
    def __init__(self):
        self.plugins = []
>>>>>>> db7bc0e26d01433233b05f14b13fb73dbca52f97
    
    def submit_plugin(self, plugin_data):
        plugin = {
            "id": f"plugin_{len(self.plugins) + 1}",
            "name": plugin_data["name"],
<<<<<<< HEAD
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
=======
            "developer": plugin_data["developer"]
        }
        self.plugins.append(plugin)
        return plugin
>>>>>>> db7bc0e26d01433233b05f14b13fb73dbca52f97

marketplace = CommunityMarketplace()
