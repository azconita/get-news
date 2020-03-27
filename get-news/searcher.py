import requests
from xml.etree.ElementTree import fromstring
from results import SearchResult


class Searcher(object):
    def search(self, word=str):
        pass

class RSSSearcher(object):

    def __init__(self, journal):
        self.journal = journal


    def search(self, word=str):
        news = self.get_lasts_news(self.journal.rss)
        news = self.get_news_with_word(word, news)
        news = self.parse_news(news)
        return news
        

    #returns list of dict of news: {title:..., link:...}
    def parse_news(self, news=list):
        return list(map(lambda item: SearchResult(item.find("title").text, item.find("link").text), news))


    #returns list of elems in xml format, which contains the given word
    def get_news_with_word(self, word=str, news=list):
        news_with_word = []
        for item in news:
            if word.lower() in item.find("title").text.lower():
                news_with_word.append(item)
        return news_with_word


    #returns list of elems in xml format
    def get_lasts_news(self, rss=str):
        response = requests.get(rss)
        xml = fromstring(response.text)
        for ch in xml:
            items = [it for it in ch if it.tag == "item"]
        return items