from django.db import models

__author__ = 'jkonieczny'


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Pricing(models.Model):
    name = models.CharField(max_length=32)
    initial = models.DecimalField(max_digits=5, decimal_places=2)
    per_week = models.DecimalField(max_digits=5, decimal_places=2)
    added = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(null=True, blank=True)

    @property
    def enabled(self):
        return self.closed is not None

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=256)
    born = models.DateField()

    def __str__(self):
        return self.name


class BookTitleManager(models.Manager):
    def get_queryset(self):
        return super(BookTitleManager, self).get_queryset()\
            .extra(select={
                'free_entities': "SELECT count(*) FROM books_bookentity "
                                 "WHERE books_bookentity.title_id = books_booktitle.id and books_bookentity.quality > 0"
                                 "and (SELECT count(*) FROM user_loan where book_id = books_bookentity.id) = 0",
                'available_entities': "SELECT count(*) FROM books_bookentity "
                                      "WHERE books_bookentity.title_id = books_booktitle.id and books_bookentity.quality > 0"
            })


class BookTitle(models.Model):
    objects = models.Manager()
    data = BookTitleManager()
    release = models.DateTimeField()
    title = models.CharField(max_length=256)
    genre = models.ManyToManyField('Genre')
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class BookEditionManager(models.Manager):
    def get_queryset(self):
        return super(BookEditionManager, self).select_related('title')


class BookEdition(models.Model):
    title = models.ForeignKey('BookTitle', null=False)
    publisher = models.ForeignKey('Publisher')
    release = models.DateTimeField()
    isbn = models.CharField(max_length=18)
    pricing = models.ForeignKey('Pricing', null=True, blank=True)

    def __str__(self):
        return "[{0}] {1}".format(self.publisher.name, self.title.title)


class BookEntityManager(models.Manager):
    def get_queryset(self):
        return super(BookEntityManager, self).select_related('book', 'title')


class BookEntity(models.Model):
    #objects = BookEntityManager()
    book = models.ForeignKey('BookEdition')
    title = models.ForeignKey('BookTitle')
    quality = models.IntegerField()