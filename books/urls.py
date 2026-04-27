from django.urls import path
from . import views
from .views import home, detail 

urlpatterns = [
    path('', views.home, name='home'),
    path('detail_book/<int:id>/', views.detail, name='detail_book'),
   
]