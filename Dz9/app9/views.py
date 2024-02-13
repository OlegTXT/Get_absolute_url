from django.views.generic import DetailView, ListView
from .models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'



