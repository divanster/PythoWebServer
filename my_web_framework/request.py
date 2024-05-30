class Request:
    def __init__(self, method, path, headers=None):
        self.method = method
        self.path = path
        self.headers = headers if headers else {}
