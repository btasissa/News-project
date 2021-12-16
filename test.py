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

    def test_get_images(self):
        self.assertEqual(self.newspaper.get_images(self.article),
                         ['https://static01.nyt.com/images/2019/02/05/multimedia/author-melina-delkic/author-melina-delkic-thumbLarge.png', 'https://static01.nyt.com/images/2021/12/17/world/17ambriefing-asia-travel/merlin_199349271_4e28e594-a23f-4b6d-a3a7-6f7f0b26190b-articleLarge.jpg?quality=75&auto=webp&disable=upscale', 'https://static01.nyt.com/images/2021/12/17/world/121721ambriefing-asia-promo/121721ambriefing-asia-promo-facebookJumbo-v2.jpg', 'https://static01.nyt.com/images/2021/12/17/world/121721ambriefing-asia-promo/121721ambriefing-asia-promo-facebookJumbo-v2.jpg'])

    def test_frequently_used_words(self):
        self.assertEqual(self.newspaper.get_frequent_words(self.article, 3), ['france', 'omicron', 'britain'])
        

    def test_get_people(self):
        self.assertEqual(self.newspaper.get_people(self.article),
                         ['Omicron', 'Jean Castex', 'Emmanuel Macron', 'Omicron'])

    def test_get_sentiment(self):
        self.assertEqual(self.newspaper.get_sentiment(self.article), "Negative")
        
    # sections and get_articles_url cannot be tested automatically because 
    # sections method handle user interaction to select the section and
    # get_articles_url method extract all the articles url related to specific section and every day articles change for every section


if __name__ == '__main__':
    unittest.main()

