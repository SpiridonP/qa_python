# qa_python
Приложение BooksCollector позволяет установить жанр книг и добавить их в избранное. 
Для данного приложения были написаны юнит-тесты. Для написания тест кейсов использовался фреймворк pytest и создавались фикстуры

Ниже описаны названия тестов

1) **def test_genre_first_version_is_true(self):**
   Проверка списка жанров

2) **def test_genre_age_rating_first_version_is_true(self):**
   Проверка списка возрасных жанров

3) **def test_add_new_book_book_without_genre(self):**
   Проверка, что книга добавляется в books_genre (словарь)

4) **def test_add_new_book_max_syblols_is_40(self):**
   Проверка, что макс кол-во символов названия книги 40

5) **def test_add_new_book_onese_is_true(self):**
   Проверка добавления одной и той же книги (книга добавится только 1 раз)

6) **def test_set_book_genre_if_book_in_books_genre_and_genre_in_genre(self):**
   Проверка добавления жанра в словарь books_genre (ключ = название книги)

7) **def test_get_book_gener_gener_is_equal_name(self):
   Проверка получения жанра по названию книги

8) **def test_get_books_gener_actual(self):
   Проверка получения словаря books_genre

9) **def test_add_book_in_favorites_is_true(self):
   Проверка добавления книги в список favorites

10) **def test_delete_book_from_favorites_is_true(self):
   Проверка удаления книги из списка favorites

11) **def test_get_list_of_favorites_books_return_favorite_books(self):**
   Проверка вывода актуального списка favorite

12) **def test_get_books_for_children_books_for_children_added(self):**
   Проверка получения книг, разрешенные детям

13) **def test_get_books_with_specific_genre_added(self):**
   Проверка списка книг с определённым жанром
   