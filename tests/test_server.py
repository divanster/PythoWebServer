import unittest
from http.server import HTTPServer
from my_web_framework.server import SimpleHTTPRequestHandler, run
from my_web_framework.router import Router

class TestServer(unittest.TestCase):
    def setUp(self):
        self.router = Router()
        self.server = HTTPServer(('localhost', 0), SimpleHTTPRequestHandler)

    def test_server_running(self):
        self.assertTrue(isinstance(self.server, HTTPServer))

if __name__ == '__main__':
    unittest.main()
