from django.test import TestCase

# Create your tests here.

from catalog.models import Author, Genre, Language, Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title = 'Книга', summary = 'Описание', isbn = '1111111111111')


    def test_title_label(self):
        book = Book.objects.get(id = 1)
        fields_name = book._meta.get_field('title').verbose_name
        self.assertEqual(fields_name, 'title')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_author_label(self):
        book = Book.objects.get(id=1)
        get_fields = book._meta.get_field('author').verbose_name
        self.assertEqual(get_fields, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        get_fields = book._meta.get_field('summary').verbose_name
        self.assertEqual(get_fields, 'summary')

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEqual(max_length, 1000)

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        get_fields = book._meta.get_field('isbn').verbose_name
        self.assertEqual(get_fields, 'ISBN')

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        get_fields = book._meta.get_field('genre').verbose_name
        self.assertEqual(get_fields, 'genre')

    def test_language_label(self):
        book = Book.objects.get(id=1)
        get_fields = book._meta.get_field('genre').verbose_name
        self.assertEqual(get_fields, 'genre')

    def test_object_name_is_title(self):
        book = Book.objects.get(id = 1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id = 1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name = 'Русский')

    def test_name_label(self):
        language = Language.objects.get(id = 1)
        fields_name = language._meta.get_field('name').verbose_name
        self.assertEqual(fields_name, 'name')

    def test_name_max_lenght(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name = 'Приключение')

    def test_name_label(self):
        genre = Genre.objects.get(id = 1)
        fields_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(fields_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id = 1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_last_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '{0} {1}'.format(author.first_name, author.last_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/catalog/authors/1')