from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from clubs.models import Clubs


def apply_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')
    return render(request, 'register/apply_club.html')

def individual_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    if request.method == "POST":
        club_id = request.POST.get("club_id")

        if not club_id:  # nothing selected
            return redirect(reverse('home') + '#section_3')

        club = get_object_or_404(Clubs, id=club_id)
        return render(request, 'individual_club.html', {"club": club})

    # if someone goes here directly
    return redirect(reverse('home') + '#section_3')

def budget_request(request):
    return render(request, 'budget_request.html')

def election_club(request):
    return render(request, 'election_club.html')