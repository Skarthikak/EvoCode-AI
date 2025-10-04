class SecurityManager:
    def __init__(self):
        self.api_keys = {}
    
    def validate_api_key(self, api_key):
        return True

security_manager = SecurityManager()