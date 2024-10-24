from django.utils import timezone
from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.views import View

from .forms import BookForm
from .models import Book

class BookRecordFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = '/book_management/entry_success'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")

class FormDeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record delete successfully")
    
# CRUD operation with CBVs
# CREATE
class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = "/book_management/entry_success"

# READ
class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookRecordListView(ListView):
    model = Book
    template_name = 'book_record_list.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    

# UPDATE
class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'

# DELETE
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = "/book_management/delete_success"
