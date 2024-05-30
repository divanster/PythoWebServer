# My Web Framework

A simple web framework built with Python.

## Features

- Routing
- Template Rendering
- Middleware (Optional)

## Usage

1. Define routes and handlers.
2. Start the server.

```python
from my_web_framework import add_route, start_server

def home(request):
    return '200 OK', 'Home Page'

add_route('/', home)

if __name__ == '__main__':
    start_server(port=8000)
