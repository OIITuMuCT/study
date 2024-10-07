from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Book
from .utils import average_rating


def index(request):
    name = 'world'
    return render(request, 'base.html' , {'name': name})

def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, 'search-results.html',
                  {'search_text': search_text})

class HomePage(TemplateView):
    template_name = 'home_page.html'


def welcome_view(request):
    return render(request, 'base.html')

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
    context = {
        'book_list': book_list
    }
    return render(request, 'myapp/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, 'myapp/book_detail.html', context)



def survey(request):
    question = 'question 1'
    answer = 'answer 1'
    list_answer = [i for i in range(1, 4)]
    return render(request, 'survey/index.html', {
        'question': question,
        'answer': answer,
        'list_answer': list_answer}
    )