from django.urls import path
from .views import individual_club 
from .views import submit_membership_application
from .views import budget_request 
from .views import election_club 
from .views import get_club_achievement, member_list, get_club_applicants, club_detail

from .views import create_event # url ng create event to, import mo muna sa views.url bago ka magdagdag ng path sa pattern

urlpatterns =[
    path('individual_club/', individual_club, name='individual_club'),
    path('individual_club/<int:club_id>/', club_detail, name='club_detail'),
    path('apply_club/<int:club_id>/', submit_membership_application, name='apply_club'),
    path('budget_request/', budget_request, name='budget_request'),
    path('election_club/<int:club_id>/', election_club, name='election_club'),
    path('achievements/<int:club_id>/', get_club_achievement, name='club_achievement'),
    path('club_applicants/<int:club_id>/', get_club_applicants, name='club_applicants'),
    path('member_list/', member_list, name='member_list'),
    path('create_event/', create_event, name='create_event'), # yung laman ng name variable and pwede mong gamitin sa {% url 'value_ng_name_variable'%}, pwede mo na gamitin to as url check mo yung page tas gamitin mo.
]