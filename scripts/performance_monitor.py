import time
import psutil
import json
from datetime import datetime

class PerformanceMonitor:
    def __init__(self):
        self.metrics_history = []
    
    def collect_system_metrics(self):
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent,
            "active_evolution_cycles": self.get_active_cycles()
        }
        
        self.metrics_history.append(metrics)
        return metrics
    
    def get_active_cycles(self):
        return len([m for m in self.metrics_history 
                   if (datetime.now() - datetime.fromisoformat(m['timestamp'])).seconds < 3600])
    
    def assess_performance_health(self):
        recent_metrics = self.metrics_history[-10:] if self.metrics_history else []
        
        if not recent_metrics:
            return {"status": "unknown", "message": "No metrics collected"}
        
        avg_cpu = sum(m['cpu_percent'] for m in recent_metrics) / len(recent_metrics)
        avg_memory = sum(m['memory_percent'] for m in recent_metrics) / len(recent_metrics)
        
        health_status = "healthy"
        if avg_cpu > 80 or avg_memory > 85:
            health_status = "critical"
        elif avg_cpu > 60 or avg_memory > 70:
            health_status = "warning"
        
        return {
            "status": health_status,
            "average_cpu": round(avg_cpu, 2),
            "average_memory": round(avg_memory, 2),
            "active_cycles": recent_metrics[-1]['active_evolution_cycles'] if recent_metrics else 0
        }
    
    def generate_performance_report(self):
        current_metrics = self.collect_system_metrics()
        health_assessment = self.assess_performance_health()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "current_metrics": current_metrics,
            "health_assessment": health_assessment,
            "recommendations": self.generate_recommendations(health_assessment)
        }
        
        with open('performance_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        return report
    
    def generate_recommendations(self, health):
        recommendations = []
        
        if health['status'] == 'critical':
            recommendations.extend([
                "Scale back evolution cycles",
                "Optimize memory usage",
                "Consider infrastructure upgrade"
            ])
        elif health['status'] == 'warning':
            recommendations.extend([
                "Monitor resource usage closely",
                "Optimize algorithm efficiency",
                "Consider caching strategies"
            ])
        else:
            recommendations.append("System operating optimally - continue current evolution pace")
        
        return recommendations

if __name__ == "__main__":
    monitor = PerformanceMonitor()
    report = monitor.generate_performance_report()
    print(f"Performance Status: {report['health_assessment']['status']}")
