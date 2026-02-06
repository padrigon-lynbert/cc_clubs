from django.urls import path
from .views import terms_and_conditions, home # landing page
# from .views import bridge # view club
from .views import login_from_landing, logout # session
from .views import global_announcements, profile_settings #individual pages with functions
from .views import login_page, upcoming_events, render_notification
from .views import verify_otp


urlpatterns = [
    path('', home, name='home'),
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
    path('home', home, name='home'),
    path('login_from_landing', login_from_landing, name='login_from_landing'),
    path('logout', logout, name='logout'),
    # path('bridge', bridge, name='bridge'),
    path('global_announcements', global_announcements, name='global_announcements'),
    path('profile_settings', profile_settings, name='profile_settings'),
    path('login_page' , login_page, name='login_page'),
    path('upcoming_events', upcoming_events, name='upcoming_events'),
    path('verify_otp', verify_otp, name='verify_otp'),
    path('notification/<int:application_id>/', render_notification, name="render_notification"),
]