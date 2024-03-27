import pytest
from main import BooksCollector
from tests import book_name_1
from tests import book_name_4
from tests import book_genre_1
from tests import book_genre_2


@pytest.fixture
def add_new_book():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    return collector

@pytest.fixture
def get_book():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    collector.set_book_genre(book_name_1, book_genre_1)
    return collector

@pytest.fixture
def favorite():
    collector = BooksCollector()
    collector.add_new_book(book_name_4)
    return collector

@pytest.fixture
def favorite_delete():
    collector = BooksCollector()
    collector.add_new_book(book_name_4)
    collector.add_book_in_favorites(book_name_4)
    return collector

@pytest.fixture
def specific():
    collector = BooksCollector()
    collector.add_new_book(book_name_4)
    collector.set_book_genre(book_name_1, book_genre_2)

@pytest.fixture
def set_book_genre():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    return collector

@pytest.fixture
def get_book_gener_actual():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    return collector