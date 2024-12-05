from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.BookListCreateAPIView.as_view(), name='book_list_create_api'),
    path('api/books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book_detail_api'),
] 