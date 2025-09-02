from django.urls import path
from .views import individual_club # view club
from .views import apply_club # no backend yet
from .views import budget_request # no backend, no acceptance page
from .views import election_club # only for linking the page
from .views import get_club_achievement, dashboard, member_list, get_club_applicants, club_detail

urlpatterns =[
    path('individual_club/', individual_club, name='individual_club'),
    path('individual_club/<int:club_id>/', club_detail, name='club_detail'),
    path('apply_club/', apply_club, name='apply_club'),
    path('budget_request/', budget_request, name='budget_request'),
    path('election_club/<int:club_id>/', election_club, name='election_club'),
    path('achievements/<int:club_id>/', get_club_achievement, name='club_achievement'),
    path('individual_club/<int:club_id>/', dashboard, name='dashboard'),
    path('club_applicants/<int:club_id>/', get_club_applicants, name='club_applicants'),
    path('member_list/', member_list, name='member_list'),
]