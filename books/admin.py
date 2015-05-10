from django.db import models
from books.models import *
from django.contrib import admin


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Genre, GenreAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Publisher, PublisherAdmin)


class PricingAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial', 'per_week')
admin.site.register(Pricing, PricingAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'born',)
admin.site.register(Author, AuthorAdmin)


class BookTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(BookTitle, BookTitleAdmin)


class BookEditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'isbn', 'pricing',)
admin.site.register(BookEdition, BookEditionAdmin)


class BookEntityAdmin(admin.ModelAdmin):
    list_display = ('book', 'title', 'quality',)

admin.site.register(BookEntity, BookEntityAdmin)