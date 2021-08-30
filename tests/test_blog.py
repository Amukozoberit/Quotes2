from datetime import datetime
from app.models import Article
import unittest

class test_Article(unittest.TestCase):
    def setUp(self):
        self.new_article=Article(article_body="Hello world",title='Flask Code',time=datetime.utcnow)
    def  test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
