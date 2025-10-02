from django.urls import path
from .views import individual_club 
from .views import submit_membership_application
from .views import budget_request 
from .views import election_club 
from .views import get_club_achievement, member_list, get_club_applicants, club_detail, accept_membership_application, rejecT_membership_application

from .views import create_event # url ng create event to, import mo muna sa views.url bago ka magdagdag ng path sa pattern

urlpatterns =[
    path('individual_club/', individual_club, name='individual_club'),
    path('individual_club/<int:club_id>/', club_detail, name='club_detail'),
    path('submit_membership_application/<int:club_id>/', submit_membership_application, name='submit_membership_application'),
    path('budget_request/', budget_request, name='budget_request'),
    path('election_club/<int:club_id>/', election_club, name='election_club'),
    path('achievements/<int:club_id>/', get_club_achievement, name='club_achievement'),
    path('club_applicants/<int:club_id>/', get_club_applicants, name='club_applicants'),
    path('club_applicants/accept/<int:application_id>/', accept_membership_application, name='accept_membership_application'),
    path('club_applicants/reject/<int:application_id>/', rejecT_membership_application, name='rejecT_membership_application'),
    path('member_list/', member_list, name='member_list'),
    path('create_event/<int:club_id>/', create_event, name='create_event')

]