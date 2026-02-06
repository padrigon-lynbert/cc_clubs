from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ClubApplicationForm
from django.db import IntegrityError, transaction
from .models import Clubs, ClubApplication, Memberships
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

    user = get_object_or_404(Users, acc_no=member_id)

    # ---- Role Restriction ----
    if user.role not in [Users.Role.STUDENT, Users.Role.OFFICER, Users.Role.ADMIN]:
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
                applicant = Users.objects.get(acc_no=applicant_id)
                new_club_registration.submitted_by = applicant
                new_club_registration.save()
                messages.success(request, 'Successfully submitted a club application form.')
                return redirect('register_club')
            except Users.DoesNotExist:
                messages.error(request, 'Session expired. Please login again.')
                return redirect('home')
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

    user = get_object_or_404(Users, acc_no=member_id)

    # ---- Role Restriction ----
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.ADMIN]:
        messages.error(request, "You are not allowed to access this page.")
        return redirect(reverse('home') + '#section_3')
    
    pending_applications = ClubApplication.objects.filter(status=0)
    total_pending = ClubApplication.objects.filter(status=0).count()
    total_accepted = ClubApplication.objects.filter(status=1).count()
    total_rejected = ClubApplication.objects.filter(status=2).count()
    total_all = ClubApplication.objects.all().count() 
    context = {
                'pending_applications': pending_applications,
                'total_pending': total_pending,
                'total_accepted': total_accepted,
                'total_rejected': total_rejected,
                'total_all': total_all,
                'approved_apps': ClubApplication.objects.filter(status=1),  
                'declined_apps': ClubApplication.objects.filter(status=2),  
            }
    return render(request, 'club_applications_review.html', context)

def accept_club(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, acc_no=member_id)
    # ---- Role Restriction ----
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.ADMIN]:
        messages.error(request, "You are not allowed to access this page.")
        return redirect(reverse('home') + '#section_3')
    
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    club_application = get_object_or_404(ClubApplication, id=club_id)
    try:
        with transaction.atomic():
            club = Clubs.objects.create(
                club_name = club_application.club_name,
                acronym = club_application.acronym,
                chairperson = club_application.submitted_by,
                adviser = club_application.adviser,
                banner = club_application.banner,
                year_level = club_application.year_level,
                email = club_application.email,
                program = club_application.program,
                description = club_application.description,
            )
            club_application.status = ClubApplication.Status.APPROVED
            club_application.save()
            messages.success(request, 'Club is successfully accepted.')

            Memberships.objects.get_or_create(
                student=club_application.submitted_by,
                club=club,
                is_officer=True,
            )

    except IntegrityError as e:
        messages.error(request, e)
    except Exception as e:
        messages.error(request, f'Something went wrong {e}')

    return redirect('get_club_application')

def reject_club(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, acc_no=member_id)
    # ---- Role Restriction ----
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.ADMIN]:
        messages.error(request, "You are not allowed to access this page.")
        return redirect(reverse('home') + '#section_3')
    
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    club_application = get_object_or_404(ClubApplication, id=club_id)

    rejection_reason = request.POST.get('rejection_reason').strip()

    if len(rejection_reason) < 5:
        messages.error(request, "Please provide a valid rejection reason (at least 5 characters).")
        return redirect('get_club_application')

    try:
        with transaction.atomic():
            club_application.status = ClubApplication.Status.REJECTED
            club_application.rejection_reason = rejection_reason
            club_application.save()
            messages.warning(request, 'Application has been rejected.')
    except Exception as e:
        messages.error(request, f'Something went wrong {e}')
    
    return redirect('get_club_application')
