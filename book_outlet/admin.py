from django.contrib import admin

from .models import Book, Author, Address, Country
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


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name",)
    # Adding more cols/headers to table in admin
    list_display = ("first_name", "last_name",)

class AddressAdmin(admin.ModelAdmin):
    list_filter = ("street", "postal_code", "city",)
    # Adding more cols/headers to table in admin
    list_display = ("street", "postal_code", "city",)


# basics for getting model into admin
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)

