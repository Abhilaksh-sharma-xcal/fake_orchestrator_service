from ray import serve
from service_1.deployment import HelloService0

app = HelloService0.bind()


@serve.deployment
class Binder:
    def __init__(self, msg):
        print("HelloService initialized")
        from service_1.deployment import HelloService1
        self.msg.bind()

    async def __call__(self, request):
        return {"message": "Hello from repo-hello-service"}


app = Binder.bind()