from urllib.parse import parse_qs


class Request:
    def __init__(self, method, path, headers=None, body=None):
        self.method = method
        self.path = path
        self.headers = headers if headers else {}
        self.body = body

    def parse_body(self):
        if self.body:
            return {key: values[0] for key, values in parse_qs(self.body.decode()).items()}
        return {}
