from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',BookListView.as_view(), name= 'book_list'),
    path('<uuid:pk>',BookDetailView.as_view(), name= 'book_detail'),
]