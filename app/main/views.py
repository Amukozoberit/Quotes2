

from . import main



#views

@main.route('/')
def index():
    return '<h1>Hello world</h1>'