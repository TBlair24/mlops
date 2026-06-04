from locust import HttpUser, task, between

class MLOpsUser(HttpUser):
    """Simulates a user interacting with the MLOps application."""

    wait_time = between(1, 3)

    @task(3)
    def home(self):
        """Hit the home endpoint."""
        self.client.get("/")

    @task(5)
    def add(self):
        """Hit the add endpoint"""
        self.client.get("/add?x=5&y=3")

    @task(2)
    def subtract(self):
        """Hit the subtract endpoint"""
        self.client.get("/subtract?x=10&y=4")

    @task(1)
    def multiply(self):
        """Hit the multiply endpoint"""
        self.client.get("/multiply?x=6&y=7")