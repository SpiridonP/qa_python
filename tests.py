from main import BooksCollector
from main import BooksCollector
book_name_1 = 'Повесть о "Человеке-Драконе"'
book_name_2 = 'Повесть о "Человеке-Драконе 2: Новое начало"'
book_name_3 = 'Повесть о "Человеке-Драконе"'
book_name_4 = 'Человек - дракон: Восстание'
book_genre_1 = 'Фантастика'
book_genre_2 = 'Ужасы'
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2



    def test_add_new_book_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book(book_name_1)
        assert book_name_1 in collector.books_genre

    def test_add_new_book_max_syblols_is_40(self):
        collector = BooksCollector()
        collector.add_new_book(book_name_2)
        assert book_name_2 not in collector.books_genre

    def test_add_new_book_onese_is_true(self):
        collector = BooksCollector()
        collector.add_new_book(book_name_3)
        assert book_name_3 in collector.books_genre

    def test_set_book_genre_if_book_in_books_genre_and_genre_in_genre(self, add_new_book):
        add_new_book.set_book_genre(book_name_1, book_genre_1)
        assert add_new_book.books_genre[book_name_1] == book_genre_1

    def test_get_book_gener_gener_is_equal_name(self, get_book_gener_actual):
        get_book_gener_actual.set_book_genre(book_name_1, book_genre_1)
        assert get_book_gener_actual.get_book_genre(book_name_1) == book_genre_1

    def test_get_books_gener_actual(self, get_book):
        get_book.get_books_genre()
        assert get_book.books_genre == {'Повесть о "Человеке-Драконе"': 'Фантастика'}

    def test_add_book_in_favorites_is_true(self, favorite):
        favorite.add_book_in_favorites(book_name_4)
        assert book_name_4 in favorite.favorites

    def test_delete_book_from_favorites_is_true(self, favorite_delete):
        favorite_delete.delete_book_from_favorites(book_name_4)
        assert book_name_4 not in favorite_delete.favorites

    def test_get_list_of_favorites_books_return_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book(book_name_1)
        collector.set_book_genre(book_name_1, book_genre_1)
        collector.add_book_in_favorites(book_name_1)
        collector.get_list_of_favorites_books()
        assert book_name_1 in collector.get_list_of_favorites_books()

    def test_get_books_for_children_books_for_children_added(self):
        collector = BooksCollector()
        book_name_5 = 'Последний маг воздуха'
        genre_3 = 'Мультфильмы'
        collector.add_new_book(book_name_5)
        collector.set_book_genre(book_name_5, genre_3)
        expected_children_books = []
        for name, genre in collector.get_books_genre().items():
            if genre not in collector.genre_age_rating and genre in collector.genre:
                expected_children_books.append(book_name_5)
        assert collector.get_books_for_children() == expected_children_books

    def test_get_books_with_specific_genre_added(self):
        collector = BooksCollector()
        books_with_specific_genre = []
        book_name_6 ='Приключения супергероя'
        genre_4 = 'Комедии'
        collector.add_new_book(book_name_6)
        collector.set_book_genre(book_name_6, genre_4)
        for name, book_genre in collector.get_books_genre().items():
            if book_genre == genre_4:
                books_with_specific_genre.append(name)
        assert collector.get_books_with_specific_genre(genre_4)

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()