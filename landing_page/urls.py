from django.urls import path
from .views import terms_and_conditions, home # landing page
from .views import register_club, bridge # view club
from .views import apply_club # inside club (indv)


urlpatterns =[
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
    path('home', home, name='home'),
    path('register_club', register_club, name='register_club'),
    path('bridge', bridge, name='bridge'),
    path('apply_club', apply_club, name='apply_club'),
]