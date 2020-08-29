from django.shortcuts import render
from django.db.models import Q
from django.views.generic import *
from django.urls import reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin)
from .models import *

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(
    LoginRequiredMixin, 
    PermissionRequiredMixin,
    DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'book.special_status'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Book.objects.filter(
            Q(title__icontains = query) | Q(title__icontains = query)
        )