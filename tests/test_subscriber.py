from datetime import datetime
from app.models import Subscriber
import unittest

class test_Subscriber(unittest.TestCase):
    def setUp(self):
        self.new_sub=Subscriber(email='mwasheb@gmail.com')
    def  test_instance(self):
        self.assertTrue(isinstance(self.new_sub,Subscriber))
