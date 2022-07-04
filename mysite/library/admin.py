from django.contrib import admin

# Register your models here.
from .models import (Author,
                     Genre,
                     Book,
                     BookInstance,
                     BookReview)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # išjungia placeholder'ius
    can_delete = False
    readonly_fields = ('unique_id',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genre')
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'book', 'reader', 'due_back', 'status')
    search_fields = ('unique_id', 'book__title')
    list_filter = ('book', 'status')
    list_editable = ('due_back', 'status', 'reader', )

    fieldsets = (
        ('General', {'fields': ('unique_id', 'book', 'reader')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')


admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookReview)

