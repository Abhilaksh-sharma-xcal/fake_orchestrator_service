from ray import serve
from service_1.deployment import HelloService_0

app = HelloService_0.bind()
