from my_web_framework import add_route, start_server
from my_web_framework.templates.engine import TemplateEngine

template_engine = TemplateEngine()


def home(request):
    context = {'title': 'Home', 'message': 'Welcome to the Home Page'}
    body = template_engine.render('home.html', context)
    return '200 OK', body


def about(request):
    return '200 OK', 'This is the About Page'


def contact(request):
    return '200 OK', 'This is the Contact Page'


add_route('/', home)
add_route('/about', about)
add_route('/contact', contact)

if __name__ == '__main__':
    start_server(port=8000)
