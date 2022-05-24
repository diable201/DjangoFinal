from django.contrib import admin
from core.models import Book, Journal, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'price',
        'description',
        'created_at',
        'num_pages',
        'genre'
    )
    list_editable = ('price',)
    list_filter = ('price',)


@admin.register(Journal)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'price',
        'description',
        'created_at',
        'journal_type',
        'publisher'
    )
    list_editable = ('price',)
    list_filter = ('price',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
    )
    list_filter = ('name',)
