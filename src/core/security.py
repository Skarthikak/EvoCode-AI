<<<<<<< HEAD
import time
from datetime import datetime, timedelta

class SecurityManager:
    def __init__(self):
        self.api_keys = {}
        self.rate_limits = {}
        self.suspicious_activities = []
    
    def validate_api_key(self, api_key):
        if api_key in self.api_keys:
            key_data = self.api_keys[api_key]
            
            if key_data.get('expires_at') and datetime.now() > key_data['expises_at']:
                del self.api_keys[api_key]
                return False
            
            return True
        
        return False
    
    def check_rate_limit(self, user_id, endpoint):
        current_time = time.time()
        key = f"{user_id}:{endpoint}"
        
        if key not in self.rate_limits:
            self.rate_limits[key] = []
        
        window_start = current_time - 3600
        
        self.rate_limits[key] = [t for t in self.rate_limits[key] if t > window_start]
        
        if len(self.rate_limits[key]) >= 100:
            self.record_suspicious_activity(user_id, endpoint, "rate_limit_exceeded")
            return False
        
        self.rate_limits[key].append(current_time)
        return True
    
    def record_suspicious_activity(self, user_id, endpoint, activity_type):
        activity = {
            "user_id": user_id,
            "endpoint": endpoint,
            "activity_type": activity_type,
            "timestamp": datetime.now().isoformat(),
            "ip_address": "0.0.0.0"
        }
        
        self.suspicious_activities.append(activity)
    
    def generate_security_report(self):
        recent_activities = [a for a in self.suspicious_activities 
                           if datetime.now() - datetime.fromisoformat(a['timestamp']) < timedelta(hours=24)]
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_api_keys": len(self.api_keys),
            "active_rate_limits": len(self.rate_limits),
            "suspicious_activities_24h": len(recent_activities),
            "security_level": self.calculate_security_level(recent_activities)
        }
    
    def calculate_security_level(self, recent_activities):
        if len(recent_activities) == 0:
            return "high"
        elif len(recent_activities) <= 5:
            return "medium"
        else:
            return "low"

security_manager = SecurityManager()
=======
class SecurityManager:
    def __init__(self):
        self.api_keys = {}
    
    def validate_api_key(self, api_key):
        return True

security_manager = SecurityManager()
>>>>>>> db7bc0e26d01433233b05f14b13fb73dbca52f97
