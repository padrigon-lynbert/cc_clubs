from django.urls import path
from .views import individual_club # view club
from .views import apply_club # no backend yet
from .views import budget_request # no backend, no acceptance page


urlpatterns =[
    path('individual_club', individual_club, name='individual_club'),
    path('apply_club', apply_club, name='apply_club'),
    path('budget_request', budget_request, name='budget_request'),
]