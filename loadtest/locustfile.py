# TODO: Locust load test
# from locust import HttpUser, task
# Hit /health and /api/nodes endpoints

from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def health(self):
        self.client.get("/health")

    @task(1)
    def get_nodes(self):
        self.client.get("/api/nodes")