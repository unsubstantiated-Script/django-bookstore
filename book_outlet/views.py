from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg


# Create your views here.

def index(request):
    # Adding in sort functionality minus means descending
    books = Book.objects.all().order_by("-rating")
    # To avoid hitting the DB too often
    num_books = books.count()
    # Could potentially have multiple avg statements
    avg_rating = books.aggregate(Avg('rating'))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating['rating__avg']
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
