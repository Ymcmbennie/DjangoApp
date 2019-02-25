from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='community-home'),
    path('about/', views.about, name='community-about'),
]