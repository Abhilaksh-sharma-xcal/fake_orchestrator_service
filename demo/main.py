from ray import serve
from service_1.deployment import HelloService

app = HelloService.bind()
