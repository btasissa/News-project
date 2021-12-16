import unittest
from final_project import *

class Test(unittest.TestCase):

    def setUp(self):
        self.newspaper = Newspaper()
        self.article = self.newspaper.get_article(
            "https://www.nytimes.com/2021/12/16/briefing/omicron-outbreaks-eu-russia-nato.html")
        print(self.newspaper.get_images(self.article))
        print(self.newspaper.get_authors(self.article))

    def test_get_title(self):
        self.assertEqual(self.newspaper.get_title(self.article), "Your Friday Briefing: France Limits U.K. Travel")

   def test_get_article_url(self):
        self.assertEqual(self.newspaper.get_article_url(self.article),
                         "https://www.nytimes.com/2021/12/16/briefing/omicron-outbreaks-eu-russia-nato.html")
        
        
    def test_get_published_date(self):
        self.assertEqual(self.newspaper.get_publish_date(self.article),
                         "12/16/2021")

    def test_get_authors(self):
        self.assertEqual(self.newspaper.get_authors(self.article),
                         ['Melina Delkic'])
