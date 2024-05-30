from http.server import BaseHTTPRequestHandler, HTTPServer
from .request import Request


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.router = kwargs.pop('router')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        request = Request(self.command, self.path)
        handler = self.router.get_handler(request.path)
        status, body = handler(request)
        self.send_response(int(status.split()[0]))
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body.encode())


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
