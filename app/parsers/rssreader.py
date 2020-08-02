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
        return BeautifulSoup(text, 'html.parser')

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
