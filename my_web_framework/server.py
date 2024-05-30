from http.server import BaseHTTPRequestHandler, HTTPServer

from .request import Request


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.router = kwargs.pop('router')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path.startswith('/static/'):
            self.serve_static()
        else:
            headers = {key: value for key, value in self.headers.items()}
            request = Request(self.command, self.path, headers)
            handler = self.router.get_handler(request.path)
            status, body = handler(request)
            self.send_response(int(status.split()[0]))
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(body.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        headers = {key: value for key, value in self.headers.items()}
        request = Request(self.command, self.path, headers, body)
        handler = self.router.get_handler(request.path)
        status, body = handler(request)
        self.send_response(int(status.split()[0]))
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body.encode())

    def serve_static(self):
        try:
            file_path = self.path.lstrip('/')
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()


def run(router, port=8000):
    server_address = ('', port)
    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(*args, router=router, **kwargs)
    httpd = HTTPServer(server_address, handler)
    print(f'Starting server on port {port}...')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        httpd.server_close()

    print("Server stopped.")
