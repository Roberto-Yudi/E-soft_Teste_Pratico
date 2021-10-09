from django.urls import path
from .views import HomePageView, SignupView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('signup/', SignupView, name='signup'),
]