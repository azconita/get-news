import requests
from xml.etree.ElementTree import fromstring

INFOBAE = "https://www.infobae.com/feeds/rss/"
NYTIMES = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
THELOCAL = "https://feeds.thelocal.com/rss/"


def search(word=str, rss=str):
    news = get_lasts_news(rss)
    news = get_news_with_word(word, news)
    news = parse_news(news)
    return news
    

#returns list of dict of news: {title:..., link:...}
def parse_news(news=list):
    return list(map(lambda item: {"title": item.find("title").text, "link": item.find("link").text}, news))


#returns list of elems in xml format, which contains the given word
def get_news_with_word(word=str, news=list):
    news_with_word = []
    for item in news:
        if word.lower() in item.find("title").text.lower():
            news_with_word.append(item)
    return news_with_word


#returns list of elems in xml format
def get_lasts_news(rss=str):
    response = requests.get(rss)
    xml = fromstring(response.text)
    for ch in xml:
        items = [it for it in ch if it.tag == "item"]
    return items

    