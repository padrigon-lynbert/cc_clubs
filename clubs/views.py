from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ClubApplicationForm
from django.db import IntegrityError, transaction
from .models import Clubs, ClubApplication
from landing_page.models import Users

# redirect
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse

# Create your views here.


def post_registration_club(request):
    
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)

    # ---- Role Restriction ----
    if user.role in [Users.Role.INSTRUCTOR, Users.Role.ACTIVITY_COORDINATOR, Users.Role.ADMIN]:
        messages.error(request, "Non-student entities are not allowed to access this page")
        return redirect(reverse('home') + '#section_3')

    # Handle user submission
    if request.method == 'POST':
        form = ClubApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            new_club_registration = form.save(commit=False)
            applicant_id = request.session.get('member_id')
            # Save user form
            try:
                applicant = Users.objects.get(id=applicant_id)
                new_club_registration.submitted_by = applicant
                new_club_registration.save()
                messages.success(request, 'Successfully submitted a club application form.')
                return redirect('register_club')
            except Users.DoesNotExist:
                messages.error(request, 'Session expired. Please login again.')
                return redirect('landing_page')
            except IntegrityError:
                messages.error(request, 'Something went wrong. Please try again.')
        else:
            messages.error(request, 'Invalid form. Please check your form and try again.')
    else:
        form = ClubApplicationForm()
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

def get_club_application(request):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)

    # ---- Role Restriction ----
    if user.role != Users.Role.ADMIN:
        messages.error(request, "Non-admin entities are not allowed to access this page")
        return redirect(reverse('home') + '#section_3')
    
    return render(request, 'club_applications_review.html')