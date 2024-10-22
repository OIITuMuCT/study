from io import BytesIO
import datetime
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from PIL import Image
from django.core.files.images import ImageFile

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from .forms import PublisherForm, SearchForm, ReviewForm, BookMediaForm
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from django.core.exceptions import PermissionDenied


def index(request):
    name = 'world'
    return render(request, 'base.html' , {'name': name})


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(
                first_names__icontains=search
            )

            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = Contributor.objects.filter(
                last_names__icontains=search
            )

            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

    return render(
        request,
        "myapp/search-results.html",
        {"form": form, "search_text": search_text, "books": books},
    )


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


def is_staff_user(user):
    return user.is_staff

# @permission_required('edit_publisher')
@user_passes_test(is_staff_user)
def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Publisher '{}' was created".format(updated_publisher))
            else:
                messages.success(request, "Publisher '{}' was updated.".format(updated_publisher))
            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "myapp/instance-form.html", {"method": request.method, "form": form})

@login_required
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)
    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
        
        user = request.user
        if not user.is_staff and review.creator.id != user.id:
            raise PermissionDenied
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book
            
            if review is None:
                messages.success(request, 'Review for "{}" created'.format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, 'Review for "{}" updated.'.format(book))
                
            updated_review.save()
            return redirect("book_detail", book.pk)
    else:
        form = ReviewForm(instance=review)
    
    return render(request,
                  "myapp/instance-form.html",
                {
                    "form": form,
                    "instance": review,
                    "model_type": "Review",
                    "related_instance": book,
                    "related_model_type": "Book",
                },
            )


@login_required
def book_media(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "POST":
        form = BookMediaForm(request.POST, request.FILES, instance=book)
        
        if form.is_valid():
            book = form.save(False)
            
            cover = form.cleaned_data.get("cover")
            
            if cover and not hasattr(cover, "path"):
                image = Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(cover.name, image_file)
            book.save()
            messages.success(
                request, 'Book "{}" was successfully updated.'.format(book)
            )
            return redirect("book_detail", book.pk)
    else:
        form = BookMediaForm(instance=book)
    return render(
        request,
        "myapp/instance-form.html", 
        {"instance": book, "form": form, "model_type": "Book", "is_file_upload": True},
    )

@login_required
def profile(request):
    return render(request, "profile.html")


# @permission_required('view_group')
# def user_profile(request, uid):
#     user = get_object_or_404(User, id=uid)
#     permissions = user.get_all_permissions()
#     return render(request, 'user_profile.html',
#         {'user': user, "permissions": permissions})

# def veteran_user(user):
#     now = datetime.datetime.now()
#     if user.date_joined is None:
#         return False
#     return now - user.date_joined > datetime.timedelta(days=365)


# @user_passes_test
# def veteran_futures(request):
#     user = request.user
#     permissions = user.get_all_permissions()
#     return render(request, "veteran_profile.html", {'user': user, 'permissions':permissions})

# redirect_to_login(next, login_url=None, redirect_field_name="next")

def survey(request):
    question = 'question 1'
    answer = 'answer 1'
    list_answer = [i for i in range(1, 4)]
    return render(request, 'survey/index.html', {
        'question': question,
        'answer': answer,
        'list_answer': list_answer}
    )
