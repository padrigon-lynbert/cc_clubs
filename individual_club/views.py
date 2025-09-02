from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from clubs.models import Clubs, MemberApplication
from landing_page.models import Users



def apply_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')
    return render(request, 'register/apply_club.html')

def member_list(request):
    return render(request, 'member_list.html')

def individual_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    if request.method == "POST":
        club_id = request.POST.get("club_id")

        if not club_id:  # nothing selected
            return redirect(reverse('home') + '#section_3')

        club = get_object_or_404(Clubs, id=club_id)

        # ! store selected club in session
        request.session['club_id'] = club.id

        return render(request, 'individual_club.html', {"club": club})

    # if someone goes here directly
    return redirect(reverse('home') + '#section_3')


def budget_request(request):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)

    club_id = request.session.get('club_id')
    club = get_object_or_404(Clubs, id=club_id)

    # ---- Role Restriction ----
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.INSTRUCTOR]:
        messages.error(request, "You are not allowed to access this page")
        return render(request, 'individual_club.html', {"club": club})

    # ! retrieve selected club from session
    if not club_id:
        messages.error(request, "No club selected")
        return redirect(reverse('home') + '#section_3')
    
    if user.role == Users.Role.ACTIVITY_COORDINATOR:
        return render(request, 'budget_request_review.html', {"club": club}) # if activity coordinator: view budget request

    return render(request, 'budget_request.html', {"club": club}) # go to budget_request (instructor only)



def election_club(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    context = {'club': club, 'user': user}
    return render(request, 'election_club.html', context)

    
def get_club_achievement(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    context = {'club': club, 'user': user}
    return render(request, 'club-achievement.html', context)

def dashboard(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    context = {'club': club, 'user': user}
    return render(request, 'individual_club.html', context)

def get_club_applicants(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    applicant = MemberApplication.objects.filter(club=club)
    context = {'club': club, 'applicant': applicant, 'user': user}
    return render(request, 'approve_member.html', context)