"""
Модуль с реализацией различных парсеров
"""

from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class RssParser(ABC):
    """
    Абстрактный класс всех пасеров
    """

    def __init__(self, url):
        self.__url = url
        self._soup = self.__set_soup()

    def __set_soup(self):
        text = requests.get(self.__url).text
        return BeautifulSoup(text)

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_links(self):
        pass

    @abstractmethod
    def get_authors(self):
        pass

    @abstractmethod
    def get_images(self):
        pass

    @abstractmethod
    def get_descriptions(self):
        pass

    @abstractmethod
    def get_titles(self):
        pass


class DTFParser(RssParser, ABC):

    def __init__(self, url="https://dtf.ru/rss/all"):
        super().__init__(url)
        self.__items = self._soup.find_all('item')
        self.__set_all_properties()

    def __set_all_properties(self):
        self.__set_authors()
        self.__set_descriptions()
        self.__set_images()
        self.__set_links()
        self.__set_titles()

    def __set_links(self):
        self.__links = []
        for item in self.__items:
            self.__links.append(item.find('link').string.strip())

    def get_links(self):
        return self.__links

    def __set_authors(self):
        self.__authors = []
        for item in self.__items:
            self.__authors.append(item.find('author').string.strip())

    def get_authors(self):
        return self.__authors

    def __set_images(self):
        self.__images = []
        for item in self.__items:
            self.__images.append(item.find('enclosure').get_attr('url').strip())

    def get_images(self):
        return self.__images

    def __set_descriptions(self):
        self.__descriptions = []
        for item in self.__items:
            self.__descriptions.append(item.find('description').string.strip())

    def get_descriptions(self):
        return self.__descriptions

    def __set_titles(self):
        self.__titles = []
        for item in self.__items:
            self.__titles.append(item.find('title').string.strip())

    def get_titles(self):
        return self.__titles

    def __set_all(self):
        self.__all = []
        for i in range(len(self.__items)):
            item = dict()
            item['title'] = self.get_titles()[i]
            item['description'] = self.get_descriptions()[i]
            item['image'] = self.get_authors()[i]
            item['author'] = self.get_authors()[i]
            item['link'] = self.get_links()[i]
            self.__all.append(item)

    def get_all(self):
        return self.__all
