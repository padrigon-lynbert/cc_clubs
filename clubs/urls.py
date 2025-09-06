from django.urls import path
from .views import post_registration_club, ajax_fetch_all_clubs, get_club_details, get_club_application

urlpatterns = [
    path('register_club/', post_registration_club, name='register_club'), # register club
    path('ajax_fetch_all_clubs/', ajax_fetch_all_clubs, name='ajax_fetch_all_clubs'), # club repository
    path('clubs/details/<int:club_id>/', get_club_details, name='get_club_details'),
    path('club-application-review/', get_club_application, name='get_club_application'),
    path('club-application/<int:club_id>/accept/', accept_club, name='accept_club'),
    path('club-application/<int:club_id>/reject/', reject_club, name='reject_club'),
    ]