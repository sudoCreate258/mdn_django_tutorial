from django.db import models

# Create your models here.
class Genre(models.Model):
    # fields
    name = models.CharField(max_length=200, help_text='Enter a book genre')
    # metadata
    # methods 
    def __str__(self):
        return self.name

class Language(models.Model):
    # fields
    name = models.CharField(max_length=200, help_text='Select Language')
    # metadata
    # methods
    def __str__(self):
        return self.name

from django.urls import reverse

class Author(models.Model):
    # fields
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    # metadata
    class Meta:
        ordering = ['last_name', 'first_name']

    # methods
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    # fields
    title = models.CharField(max_length=200)
    ## each book can have one author but an auther can have many books
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter book description')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 char ISBN number')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    # methods
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

import uuid

class BookInstance(models.Model):
    # fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reversed'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    # meta
    class Meta:
        ordering = ['due_back']
    # methods
    def __str__(self):
        return f'{self.id} ({self.book.title})'
    def checkout_book(name)
        # check if available
        # check if user is eligible
        # populate other portions
        record = BookInstance(name)
        # save into DB
        record.save()
