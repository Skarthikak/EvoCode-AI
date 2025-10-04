class MLTrainingPipeline:
    def __init__(self):
        self.training_jobs = []
    
    def create_training_job(self, job_type):
        return {"job_id": "job_1"}

ml_pipeline = MLTrainingPipeline()