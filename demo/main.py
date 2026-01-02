from ray import serve
from service_1.deployment import HelloService0

app = HelloService0.bind()
