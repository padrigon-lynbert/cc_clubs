from django.urls import path
from .views import terms_and_conditions, home # landing page
from .views import bridge, individual_club # view club
from .views import login_from_landing, logout # session
from .views import apply_club # inside club (indv)


urlpatterns =[
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
    path('home', home, name='home'),
    path('login_from_landing', login_from_landing, name='login_from_landing'),
    path('individual_club', individual_club, name='individual_club'),
    path('logout', logout, name='logout'),
    path('bridge', bridge, name='bridge'),
    path('apply_club', apply_club, name='apply_club'),
]