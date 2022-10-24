from django.http import HttpResponse
from django.shortcuts import render
from .models import Authors, Categories, Books



def books_index(request):
    books = Books.objects.all().order_by('title')
    context = {
        "books": books,
    }
    return render(request, 'books_index.html', context)

def books_detail(request, pk):
    books = Books.objects.get(pk=pk)

    context = {
        "books": books,

    }
    return render(request, 'books_detail.html', context)

def books_category(request, categories):
    books = Books.objects.filter(categories__name_of_category__contains=categories)
    context = {
        "books": books,
        "categories": categories
    }
    return render(request, 'books_category.html', context)
