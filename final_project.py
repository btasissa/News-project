import requests
from bs4 import BeautifulSoup
from newspaper import Article
from nltk import sentiment
from string import punctuation
import nltk


class Newspaper:

    def __init__(self):
        """this method will initialize the url attribute with the url of NYT"""
        self.url = "https://www.nytimes.com"
        self.section = ""

    def sections(self):
        """
        this method will extract the sections from NYT website and ask the user to select the section and modify
        the url attribute accordingly
        return: Non
        """
        page = requests.get(self.url)
        page_soup = BeautifulSoup(page.content, 'html.parser')
        sections_url = []
        count = 1

        for anchor_tag in page_soup.find("header").find_all(class_="css-1vxc2sl")[-1].find_all("a")[:-1]:
            sections_url.append(anchor_tag.get("href"))
            print(f"{count}) {anchor_tag.text}")
            count += 1
        print("Enter Section number to search News:")
        section_number = int(input())
        self.section = sections_url[section_number - 1].split("/")[-1]
        self.url = self.url + sections_url[section_number - 1]

    def get_articles_section(self):
        """this method will return the section of NYT
                        return: section
                        """
        page = requests.get(self.url)
        page_soup = BeautifulSoup(page.content, 'html.parser')
        articles_url = []
        for anchor_tag in page_soup.find(id="stream-panel").find_all('a'):
            link = "https://www.nytimes.com" + anchor_tag.get("href")
            articles_url.append(link)

        return articles_url

    def get_articles_url(self):
        """this method will return the url of list articles url
                param: article object
                return: articles_url
                """
        page = requests.get(self.url)
        page_soup = BeautifulSoup(page.content, 'html.parser')
        articles_url = []
        for anchor_tag in page_soup.find(id="stream-panel").find_all('a'):
            link = "https://www.nytimes.com" + anchor_tag.get("href")
            articles_url.append(link)

        return articles_url

    def get_article(self, link):
        """ this method extracts all the articles from the section
        return: list of articles
        """
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()

        return article

    def get_title(self, article):
        """this method will return the title of article
        param: article object
        return: title
        """
        title = article.title
        return title

    def get_article_url(self, article):
        """this method will return the url of article
                param: article object
                return: url
                """

        article_url = article.url
        return article_url

    def get_authors(self, article):
        """this method will return the list of authors of article
        param: article object
        return: authors
        """

        authors = article.authors
        return authors

    def get_publish_date(self, article):
        """this method will return the publish date of article
            param: article object
            return: publish date
            """
        published_date = str(article.publish_date.strftime("%m/%d/%Y"))
        return published_date

    def get_summary(self,article):
        """this method will return the summary of article
                param: article object
                return: summary
                """
        summary = article.summary
        return summary

    def get_images(self,article):
        """this method will return the list of urls of images of article
                param: article object
                return: list of images url
                """
        top_image = str(article.top_image)
        images = list(article.images)
        images.append(top_image)
        return images

    def get_articles_section(self):
        """this method will return the section of NYT
                        return: section
                        """
        return self.section

    def get_sentiment(self, article: Article):
        """this method will determine if the article expresses overall positive or negative
        param: article object
        return: The overall sentiment. Positive or negative
        """
        sia = sentiment.SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(article.text)
        if sentiment_scores["compound"] > 0:
            return "Positive"
        return "Negative"
def main():
    """this method is the driver of the Newspaper class"""
    print("Welcome to the Newspaper Aggregator Project. \n"
          "Here, you will have access to all the latest articles in the New York Times.\n")

    newspaper = Newspaper()
    newspaper.sections()
    section = newspaper.get_articles_section()
    articles_url = newspaper.get_articles_url()
    counter = 0
    print(f"You are reading News from {section} section.")
    for url in articles_url:
        print("-------------------------------------------------------------------------------------------------")
        article = newspaper.get_article(url)
        print(f"Title: {newspaper.get_title(article)}")
        print(f"Article URL: {newspaper.get_article_url(article)}")
        print(f"Published Date: {newspaper.get_publish_date(article)}")
        images = newspaper.get_images(article)
        print(f"\nTop Image: {images[-1]}")
        print("Other Images of Article")
        for image in images[:-1]:
            print(image)

        authors = newspaper.get_authors(article)
        print("\nAuthor(s)")
        for author in authors:
            print(author)

        print("\nA Quick Article Summary")
        print("-------------------------------------------------------")
        print(newspaper.get_summary(article))
        print("-------------------------------------------------------")
        counter += 1
        if counter == len(articles_url):
            print("All the Articles have been successfully read!\n"
                  "Thank you")
            break

        ask = input("Enter (N/n) to read next article or Press any other key to exit:   ")
        if ask in ["N", "n"]:
            continue
        else:
            print("Thank You.")
            break


if __name__ == "__main__":
    main()