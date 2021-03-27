import unittest
from npr_news import NprNews
import json

class NprNewstest(unittest.TestCase):
    
    def test_returns_values_for_articles(self):
        articles = NprNews().get_articles()
        self.assertTrue(len(articles) > 0, "Article list is not empty")

        for article in articles:
            print(json.dumps(article.__dict__))
            self.assertIsNotNone(article.url, "Article url is not None")
            self.assertIsNotNone(article.title, "Article title is not None")

if __name__ == '__main__':
    unittest.main()
