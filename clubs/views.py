from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ClubRegistrationForm
from django.db import IntegrityError
from .models import Clubs, ClubApplication
from landing_page.models import Users

# redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def post_registration_club(request):
    # Login status checker (original just session checker)
    # if not request.session.get('member_logged_in'):
    #     messages.error(request, "You must be logged in to access this page")
    #     return HttpResponseRedirect(reverse('home') +'#section_3')
    
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)

    # ---- Role Restriction ----
    if user.role in [Users.Role.STUDENT, Users.Role.OFFICER]:
        messages.error(request, "Students are not allowed to access this page")
        return redirect(reverse('home') + '#section_3')


        
    # Handle user submission
    if request.method == 'POST':
        form = ClubRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            club_name = form.cleaned_data['club_name'].strip().lower()

            # Check if the club is already officially registered
            if Clubs.objects.filter(club_name__iexact=club_name).exists() or \
               ClubApplication.objects.filter(club_name__iexact=club_name).exists():
                messages.error(request, 'This club is already registered. Please choose a different name.')
                return redirect('register_club')

            new_club_registration = form.save(commit=False)
            instructor_id = request.session.get('member_id')
            # Save user form
            try:
                instructor = Users.objects.get(id=instructor_id)
                new_club_registration.submitted_by = instructor
                new_club_registration.save()
                messages.success(request, 'Successfully submitted a club registration form.')
                return redirect('register_club')
            except IntegrityError:
                messages.error(request, 'The club name is already applied, try a different name.')
                return redirect('register_club')
        else:
            messages.error(request, 'The club name is already applied, try a different name.')
    else:
        form = ClubRegistrationForm()
    # Render the form
    context = {'form': form}
    return render(request, 'register/register_club.html', context)


# this is about club repository and club detail fetch for the right box
def ajax_fetch_all_clubs(request):
    clubs = Clubs.objects.all().order_by('id')
    return render(request, 'club_repository/ajax_fetch_all_clubs.html', {'clubs': clubs})

from django.http import JsonResponse
from .models import Clubs

def get_club_details(request, club_id):
    try:
        club = Clubs.objects.get(id=club_id)
        data = {
            'name': club.club_name,
            'id': club.id,
            'banner': club.banner,
            # add more fields here
        }
        return JsonResponse(data)
    except Clubs.DoesNotExist:
        return JsonResponse({'error': 'Club not found'}, status=404)
