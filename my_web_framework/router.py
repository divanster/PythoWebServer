class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def get_handler(self, path):
        return self.routes.get(path, self.handle_404)

    def handle_404(self, request):
        return '404 Not Found', 'The page you are looking for does not exist.'
