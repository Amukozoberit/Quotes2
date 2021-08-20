import os


from app import create_app
from flask_script import Manager,Server



app=create_app(os.getenv('default'))
manager=Manager(app)