class LoggerMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print(f"Request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        return self.app(environ, start_response)
