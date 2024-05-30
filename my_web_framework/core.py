from .server import run
from .router import Router

router = Router()


def add_route(path, handler):
    router.add_route(path, handler)


def start_server(port=8000):
    run(router, port)
