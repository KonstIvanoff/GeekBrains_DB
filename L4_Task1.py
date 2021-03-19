import requests, time, datetime
from lxml import html
from pprint import pprint
from pymongo import MongoClient
from datetime import datetime

def save_to_mongo(data):
    # сохранение новостей в MongoDb
    mongo_url = '127.0.0.1:27017'
    mongo_db = 'mynews'

    with MongoClient(mongo_url) as cli:
        db = cli[mongo_db]
        my_collection = db.allnews
        my_collection.insert_many(data)


class NewsMailRuParing:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
        self.base_url = 'https://news.mail.ru/'
        self.xpath_str = '//div[contains(@class, "daynews__item")]'
        self.xpath_str2 = '//div[@class="js-module"]//li[@class="list__item"]'

    def parse(self):
        # запрос страницы
        qr = requests.get(self.base_url, self.headers)

        if qr.status_code == 200:
            my_doc = html.fromstring(qr.text)

            # список, куда укладываем новости
            news = []

            # главные новости
            my_news = my_doc.xpath(self.xpath_str)
            for nn in my_news:
                one_new = self.parse_main_news(nn)
                news.append(one_new)

            # новости, находящиеся ниже
            my_news = my_doc.xpath(self.xpath_str2)
            for nn in my_news:
                one_new = self.parse_other_news(nn)
                news.append(one_new)

            # pprint(news)
            # сохранение в базу
            save_to_mongo(news)

    def get_src_dt(self, url_of_new):
        # проходим по ссылке, чтобы забрать источник и дату публикации
        time.sleep(1)
        qsrcdt = requests.get(url_of_new, self.headers)

        if qsrcdt.status_code == 200:
            my_res = html.fromstring(qsrcdt.text)
            new_date = my_res.xpath('//span[@class="note"]//span[starts-with(@class,"note__text")]/@datetime')
            new_src = my_res.xpath('//span[@class="note"]/a/span/text()')
        else:
            return None, None

        return new_date[0], new_src[0]

    def parse_main_news(self, doc):
        # парсинг главных новостей
        one_new = {}
        one_new['title'] = list(doc.xpath('.//span[contains(@class,"photo__title")]/text()'))[0]
        one_new['link'] = list(doc.xpath('.//a/@href'))[0]
        one_new['date'], one_new['source'] = self.get_src_dt(one_new['link'])
        return one_new

    def parse_other_news(self, doc):
        # парсинг новостей под главными
        one_new = {}
        one_new['title'] = list(doc.xpath('.//a/text()'))[0]
        one_new['link'] = list(doc.xpath('.//a/@href'))[0]
        one_new['date'], one_new['source'] = self.get_src_dt(one_new['link'])
        return one_new


class YaComNewsParing:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
        self.base_url = 'https://yandex.com/news/'
        self.xpath_str = '//article[starts-with(@class, "mg-card")]'
        # текущая дата
        self.current = datetime.today().strftime('%d.%m.%Y')

    def parse_ya_news(self, doc):
        ya_new = {}
        ya_new['title'] = list(doc.xpath('.//div[@class="mg-card__annotation"]/text()'))[0]
        ya_new['link'] = list(doc.xpath('.//a/@href'))[0]
        ya_new['date'] = self.current + ' ' + list(doc.xpath('.//span[@class="mg-card-source__time"]/text()'))[0]
        ya_new['source'] = list(doc.xpath('.//span[@class="mg-card-source__source"]/a/text()'))[0]
        return ya_new

    def parse(self):
        qr = requests.get(self.base_url, self.headers)

        if qr.status_code == 200:
            my_doc = html.fromstring(qr.text)

            # список, куда укладываем новости
            news = []
            # все новости
            my_news = my_doc.xpath(self.xpath_str)
            for nn in my_news:
                ya_new = self.parse_ya_news(nn)
                news.append(ya_new)

            # сохранение новостей в базу
            save_to_mongo(news)


class LentaRuParing:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
        self.base_url = 'https://lenta.ru/'
        self.xpath_str = '//div[@class="item"]'
        # текущая дата
        self.current = datetime.today().strftime('%d.%m.%Y')

    def parse_lenta_news(self, doc):
        l_new = {}
        l_new['title'] = list(doc.xpath('.//a/text()'))[0]
        l_new['link'] = self.base_url + list(doc.xpath('.//a/@href'))[0]
        l_new['date'] = self.get_lenta_dt(l_new['link'])
        l_new['source'] = self.base_url
        return l_new

    def get_lenta_dt(self, lnk):
        time.sleep(1)
        dt_xpath = '//div[@class="b-topic__info"]/time/text()'
        qdt = requests.get(lnk, self.headers)

        if qdt.status_code == 200:
            dt_doc = html.fromstring(qdt.text)
            dt = list(dt_doc.xpath(dt_xpath))[0]
            return dt

        return None

    def parse(self):
        qr = requests.get(self.base_url, self.headers)

        if qr.status_code == 200:
            my_doc = html.fromstring(qr.text)

            # список, куда укладываем новости
            news = []
            # все новости
            my_news = my_doc.xpath(self.xpath_str)
            for nn in my_news:
                le_new = self.parse_lenta_news(nn)
                news.append(le_new)

            # print(news)
            # сохранение новостей в базу
            save_to_mongo(news)


my = NewsMailRuParing()
my.parse()

ya = YaComNewsParing()
ya.parse()

le = LentaRuParing()
le.parse()