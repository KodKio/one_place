from app.parsers import rssreader


class DTFParser(rssreader.RssParser, rssreader.ABC):

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
        self.__set_all()

    def __set_links(self):
        self.__links = []
        for item in self.__items:
            link = item.text[item.text.find('https://dtf'):]
            link = link[:link.find('\n')]
            self.__links.append(link)

    def get_links(self):
        return self.__links

    def __set_authors(self):
        self.__authors = []
        for item in self.__items:
            self.__authors.append(item.find('author').text)

    def get_authors(self):
        return self.__authors

    def __set_images(self):
        self.__images = []
        for item in self.__items:
            images = item.find_all('enclosure')
            flag = True
            if len(images):
                i = 0
                while i < len(images) and flag:
                    if images[i].get('type') == "image/jpeg":
                        self.__images.append(images[i].get('url'))
                        flag = False
                    i += 1
            if flag:
                self.__images.append('')

    def get_images(self):
        return self.__images

    def __set_descriptions(self):
        self.__descriptions = []
        for item in self.__items:
            description = item.find('description').text
            self.__descriptions.append(description[:description.find('\n')])

    def get_descriptions(self):
        return self.__descriptions

    def __set_titles(self):
        self.__titles = []
        for item in self.__items:
            self.__titles.append(item.find('title').text.replace('&amp;', '&'))

    def get_titles(self):
        return self.__titles

    def __set_all(self):
        self.__all = []
        for i in range(len(self.__items)):
            item = dict()
            item['title'] = self.get_titles()[i]
            item['description'] = self.get_descriptions()[i]
            item['image'] = self.get_images()[i]
            item['author'] = self.get_authors()[i]
            item['link'] = self.get_links()[i]
            self.__all.append(item)

    def get_all(self):
        return self.__all
