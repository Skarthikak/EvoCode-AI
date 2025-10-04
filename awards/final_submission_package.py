class AwardSubmissionPackage:
    def __init__(self):
        self.award_targets = {}
    
    def generate_submission_package(self):
        return {"status": "ready"}

award_package = AwardSubmissionPackage()