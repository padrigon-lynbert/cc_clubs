from django.urls import path
from .views import post_registration_club, ajax_fetch_all_clubs

urlpatterns = [
    path('register_club/', post_registration_club, name='register_club'),
    path('ajax_fetch_all_clubs/', ajax_fetch_all_clubs, name='ajax_fetch_all_clubs'),
    ]