from my_web_framework import add_route, start_server
from my_web_framework.templates.engine import TemplateEngine
from my_web_framework.users import authenticate, add_user
from my_web_framework.sessions import create_session
from my_web_framework.middleware.auth import require_auth

template_engine = TemplateEngine()

def home(request):
    context = {'title': 'Home', 'message': 'Welcome to the Home Page'}
    body = template_engine.render('home.html', context)
    return '200 OK', body

def about(request):
    return '200 OK', 'This is the About Page'

def contact(request):
    return '200 OK', 'This is the Contact Page'

def login(request):
    if request.method == 'POST':
        params = request.parse_body()
        username = params.get('username')
        password = params.get('password')
        if authenticate(username, password):
            session_id = create_session(username)
            return '200 OK', f'Logged in as {username}. Session ID: {session_id}'
        return '401 Unauthorized', 'Invalid credentials'
    else:
        body = template_engine.render('login.html', {})
        return '200 OK', body

def register(request):
    if request.method == 'POST':
        params = request.parse_body()
        username = params.get('username')
        password = params.get('password')
        success, message = add_user(username, password)
        status = '200 OK' if success else '400 Bad Request'
        return status, message
    else:
        body = template_engine.render('register.html', {})
        return '200 OK', body

add_route('/', home)
add_route('/about', about)
add_route('/contact', require_auth(contact))
add_route('/login', login)
add_route('/register', register)

if __name__ == '__main__':
    start_server(port=8000)
