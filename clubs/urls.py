from django.urls import path
from .views import post_registration_club

urlpatterns = [
    path('register_club/', post_registration_club, name='register_club'),
]