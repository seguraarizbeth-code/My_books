from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail_book/<int:id>/', views.detail_book, name='detail_book'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
]