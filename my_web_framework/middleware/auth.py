from my_web_framework.sessions import get_username


def require_auth(handler):
    def wrapped_handler(request):
        session_id = request.headers.get('Authorization')
        if not session_id or not get_username(session_id):
            return '401 Unauthorized', 'Unauthorized access. Please log in.'
        return handler(request)

    return wrapped_handler
