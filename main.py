from ray import serve
from hello_service.deployment import HelloService

app = serve.Application(
    HelloService.bind()
)
