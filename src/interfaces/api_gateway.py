class APIGateway:
    def __init__(self):
        self.request_log = []
    
    def handle_code_completion(self, data):
        return {"suggestions": ["def ", "class "]}

api_gateway = APIGateway()