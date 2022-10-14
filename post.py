import datetime

import file_manager
import utils


class Post:
    def __init__(self):
        self.__author = None
        self.__title = None
        self.__creation_date = datetime.datetime.now()
        self.__content = None

    @property
    def author(self):
        return self.__author.lower()

    @author.setter
    def author(self, value):
        record = utils.search_record("person", value)
        if not record:
            raise TypeError("author not exist as person")
        self.__author = record[2]

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, value):
        self.__content = value

    def add(self):
        record = utils.search_record(self.__class__.__name__, self.__title)
        if not record and self.__author and self.__title and self.__content:
            record = [self.__author, self.__title, self.__creation_date, self.__content]
            file_manager.add_item(self.__class__.__name__, self.__title, record)
        else:
            raise TypeError("post invalid or exist")

    def update_by_content(self, title, new_content):  # -> replace content with old content
        record = utils.search_record(self.__class__.__name__, title)
        if record:
            record[3] = new_content
            file_manager.update_item(self.__class__.__name__, title, record)
        else:
            raise TypeError("title not found")

    def update_by_title(self, old_title, new_title):
        record = utils.search_record(self.__class__.__name__, old_title)
        if record and not utils.search_record(self.__class__.__name__, new_title):
            record[1] = new_title
            file_manager.update_item(self.__class__.__name__, old_title, record)
        else:
            raise TypeError("title not found or exist")

    def delete_by_title(self, title):
        record = utils.search_record(self.__class__.__name__, title)
        if record:
            file_manager.delete_item(self.__class__.__name__, title)
        else:
            raise TypeError("title not found")