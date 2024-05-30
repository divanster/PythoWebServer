import uuid

sessions = {}


def create_session(username):
    session_id = str(uuid.uuid4())
    sessions[session_id] = username
    return session_id


def get_username(session_id):
    return sessions.get(session_id)
