from django.urls import path
from .views import individual_club 
from .views import submit_membership_application
from .views import budget_request 
from .views import election_club 
from .views import get_club_achievement, member_list, get_club_applicants, club_detail, accept_membership_application, rejecT_membership_application, achievement_create, achievement_update, achievement_delete, analyze_club
from .views import delete_announcement, create_event, display_link, edit_link, delete_link, add_link

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
    path('create_event/<int:club_id>/', create_event, name='create_event'),
    path("announcement/delete/<int:pk>/", delete_announcement, name="delete_announcement"),
    path("links/<int:club_id>/", display_link, name='display_link'),
    path('links/add/<int:club_id>/', add_link, name='add_link'),
    path('links/edit/<int:link_id>/', edit_link, name='edit_link'),
    path('links/delete/<int:link_id>/', delete_link, name='delete_link'),
    # Create achievement for a specific club
    path('<int:club_id>/achievements/create/', achievement_create, name='achievement_create'),
    # Update achievement
    path('<int:club_id>/achievements/<int:achievement_id>/update/', achievement_update, name='achievement_update'),
    # Delete achievement
    path('<int:club_id>/achievements/<int:achievement_id>/delete/', achievement_delete, name='achievement_delete'),
    # Analyze Club Performance
    path('<int:club_id>/analyze_club_performance/', analyze_club, name='analyze_club'), 
]