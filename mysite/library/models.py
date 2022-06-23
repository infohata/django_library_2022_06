from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=200, help_text='Įveskite knygos žanrą (pvz. detektyvas)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Book(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name="books")
    summary = models.TextField(verbose_name="Aprašymas", max_length=1000, help_text='Trumpas knygos aprašymas')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
    genre = models.ManyToManyField('Genre', help_text='Išrinkite žanrą(us) šiai knygai')

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all())

    display_genre.short_description = 'Genre'

    # def get_absolute_url(self):
    #     """Nurodo konkretaus aprašymo galinį adresą"""
    #     return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class BookInstance(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey(to='Book', verbose_name="Knyga", on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(verbose_name="Bus prieinama", null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Statusas')

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    class Meta:
        verbose_name = 'Book instance'
        verbose_name_plural = 'Book instances'


class Author(models.Model):
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)

    def display_books(self):
        return ', '.join(book.title for book in self.books.all())

    display_books.short_description = 'Books'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
