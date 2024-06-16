from django.contrib import admin
from.models import Author,Book,BookCategory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','author']


@admin.register(BookCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category']
        