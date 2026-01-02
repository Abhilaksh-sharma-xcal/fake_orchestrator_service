from ray import serve
from service_1.deployment import HelloService0, HelloService1

@serve.deployment
class Binder:
    def __init__(self, service0_handle, service1_handle):
        self.service0 = service0_handle
        self.service1 = service1_handle

    async def __call__(self, request):
        result0 = await self.service0.remote(request)
        result1 = await self.service1.remote(request)
        return {"service0": result0, "service1": result1}
