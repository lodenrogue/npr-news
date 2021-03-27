import requests
from bs4 import BeautifulSoup

from article import Article

BASE_URL = "https://text.npr.org"

class NprNews:

    def get_articles(self):
        main_page_resp = requests.get(BASE_URL)
        directory_soup = BeautifulSoup(main_page_resp.content, "html.parser")
        
        urls = self._get_urls(directory_soup)
        titles = self._get_titles(directory_soup)
        return self._to_articles(urls, titles)

    
    def _to_articles(self, urls, titles):
        articles = []

        for i in range(0, len(urls)):
           url = urls[i]
           title = titles[i]
           articles.append(Article(title, url))

        return articles

    
    def _get_titles(self, soup):
        links = soup.find_all("a", {"class" : "topic-title" })
        
        titles = []
        for link in links:
            titles.append(link.text)

        return titles


    def _get_urls(self, soup):
        links = soup.find_all("a", {"class" : "topic-title" })
        
        urls = []
        for link in links:
            urls.append("{}{}".format(BASE_URL, link["href"]))

        return urls


if __name__ == "__main__":
    articles = NprNews().get_articles()
    
    for article in articles:
        print("=====================================")
        print("Title:", article.title)
        print(article.url)
        print("=====================================")
        print()
