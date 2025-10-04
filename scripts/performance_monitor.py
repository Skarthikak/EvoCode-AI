class PerformanceMonitor:
    def __init__(self):
        self.metrics_history = []
    
    def collect_system_metrics(self):
        return {"cpu_percent": 45, "memory_percent": 60}

performance_monitor = PerformanceMonitor()
