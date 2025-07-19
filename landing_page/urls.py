from django.urls import path
from .views import terms_and_conditions, home # landing page
from .views import register_club, individual_club # view club


urlpatterns =[
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
    path('home', home, name='home'),
    path('register_club', register_club, name='register_club'),
    path('individual_club', individual_club, name='individual_club'),
]