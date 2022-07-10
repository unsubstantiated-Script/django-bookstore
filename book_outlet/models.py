from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street},  {self.city}, {self.postal_code}"


    class Meta:
        verbose_name_plural = "Addresses"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name}  {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    #     Connecting Author model to this...use Author in the param, on_delete allows all related books to an author to be deleted PROTECT keeps that from happening, SETNULL would set the author field to null if author deleted
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    # db_index makes searching the field faster id out of the box has index search
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)

    #many to many
    published_countries = models.ManyToManyField(Country, null=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # Don't need this with the admin stuff going on.
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    # This is needed to print data to the console vs.
    def __str__(self):
        return f"{self.title} ({self.rating})"






# Data relationships
# One to Many
# Book belongs to author
# Author might author multiple books
# That's a one-to-many relationship One Author -> Many Books

# One to One
# Author has an address

# Many to Many
# One book published in many countries. Many countries might have that same book

# Queries Double underscores drill down into the db...they also drill down into the filter modifiers as well "contains, greater than, etc...
# books_by_lewis = Book.objects.filter(author__last_name="Rowling")
# books_by_lewis = Book.objects.filter(author__last_name__contains="wling")

#Can also query the inverse relation...
# cslewis = Author.objects.get(first_name="Chris")
# getting the book from the author Django takes child class and adds "_set" to it
# cslewis.book_set.all()
