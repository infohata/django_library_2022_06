from django.shortcuts import render, get_object_or_404
from .models import (Book,
                     BookInstance,
                     Author)
from django.views import generic
from django.core.paginator import Paginator

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)


def authors(request):
    paginator = Paginator(Author.objects.all(), 1)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    my_context = {
        "authors": paged_authors,
    }
    return render(request, 'authors.html', context=my_context)


def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', context={"author": single_author})


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 1


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'
