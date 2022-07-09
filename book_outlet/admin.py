from django.contrib import admin

from .models import Book
# Register your models here.

# Getting more control over models in admin with an admin class
class BookAdmin(admin.ModelAdmin):
    # Use strings only here...
    # Making a field readonly
    # readonly_fields = ("slug", )
    # Showing what the field will be
    prepopulated_fields = {'slug': ("title",)}
    # Adding filter options
    list_filter = ("author", "rating",)
    # Adding more cols/headers to table in admin
    list_display = ("title", "author",)

# basics for getting model into admin
admin.site.register(Book, BookAdmin)