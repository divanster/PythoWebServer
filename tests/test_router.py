import unittest
from my_web_framework.router import Router

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.router = Router()

    def test_add_route(self):
        def home(request):
            return '200 OK', 'Home Page'

        self.router.add_route('/', home)
        handler = self.router.get_handler('/')
        self.assertEqual(handler(None)[1], 'Home Page')

if __name__ == '__main__':
    unittest.main()
