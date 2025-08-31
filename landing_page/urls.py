from django.urls import path
from .views import terms_and_conditions, home # landing page
from .views import bridge # view club
from .views import login_from_landing, logout # session
from .views import global_announcements, global_chat #individual pages with functions

urlpatterns =[
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
    path('home', home, name='home'),
    path('login_from_landing', login_from_landing, name='login_from_landing'),
    path('logout', logout, name='logout'),
    path('bridge', bridge, name='bridge'),
    path('global_announcements', global_announcements, name='global_announcements'),
    path('global_chat', global_chat, name='global_chat'),
]