from django.urls import path
from .views import HomePageView

urlspatterns = [
    path('', HomePageView, name='home')
]