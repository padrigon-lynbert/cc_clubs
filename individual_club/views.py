from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError, transaction
from django.http import HttpResponseNotAllowed
from clubs.models import Clubs, MemberApplication, Memberships, Achievement
from landing_page.models import Users
from .models import BudgetRequest
from .forms import MembershipApplicationForm
import requests
from clubs.models import Announcement


def submit_membership_application(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)
    club = get_object_or_404(Clubs, id=club_id)
    # ---- Role Restriction ----
    if user.role not in [Users.Role.STUDENT, Users.Role.ADMIN]:
        messages.error(request, "Non-student entities are not allowed to access this page.")
        return redirect('club_detail', club_id=club.id)
    
    # Membership checker
    if Memberships.objects.filter(student=user, club=club).exists():
        messages.error(request, "You are already a member of this club.")
        return redirect('club_detail', club_id=club.id)
    
    # Application checker
    if MemberApplication.objects.filter(student=user, club=club, status=MemberApplication.Status.PENDING).exists():
        messages.error(request, 'You have a pending application on this club')
        return redirect('club_detail', club_id=club.id)
    
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            new_member_application = form.save(commit=False)
            try:
                new_member_application.student = user
                new_member_application.club = club
                new_member_application.save()
                messages.success(request, f'You have successfully registered an application in {club.club_name}')
                return redirect('club_detail', club_id=club.id)
            except IntegrityError as error:
                messages.error(request, f'Something went wrong: {error}')
                return redirect('club_detail', club_id=club.id)
    else:
        form = MembershipApplicationForm()

    context = {'form': form, 'club': club}
    
    return render(request, 'register/apply_club.html', context)

def accept_membership_application(request, application_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
        
    user = get_object_or_404(Users, id=member_id)
    # ---- Role Restriction ----
    if user.role not in [Users.Role.OFFICER, Users.Role.INSTRUCTOR, Users.Role.ADMIN]:
        messages.error(request, "You are not allowed to access this page.")
        return redirect(reverse('home') + '#section_3')

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    member_application = get_object_or_404(MemberApplication, id=application_id)

    try:
        with transaction.atomic():
            Memberships.objects.get_or_create(
                student = member_application.student,
                club = member_application.club
            )
            member_application.status = MemberApplication.Status.APPROVED
            member_application.save()
            messages.success(request, f'{member_application.student} has been accepted into {member_application.club}.')
    except IntegrityError as e:
        messages.error(request, str(e))
    except Exception as e:
        messages.error(request, str(e))
    
    return redirect('club_applicants', club_id=member_application.club.id)

def rejecT_membership_application(request, application_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)
    # ---- Role Restriction ----
    if user.role not in [Users.Role.OFFICER, Users.Role.INSTRUCTOR, Users.Role.ADMIN]:
        messages.error(request, "You are not allowed to access this page.")
        return redirect(reverse('home') + '#section_3')
    
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    member_application = get_object_or_404(MemberApplication, id=application_id)
    try:
        with transaction.atomic():
            member_application.status = MemberApplication.Status.REJECTED
            member_application.save()
            messages.warning(request, f'Rejected membership application of {member_application.student.name}')
    except Exception as e:
        messages.error(request, f'Something went wrong: {str(e)}')
    
    return redirect('club_applicants', club_id=member_application.club.id)

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

        # store selected club
        request.session['club_id'] = club_id

        # redirect to clean URL with ID
        return redirect('club_detail', club_id=club_id)

    # if someone goes here directly without POST
    return redirect(reverse('home') + '#section_3')

# for individual club to carry id in the url
def club_detail(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    # Fetch user info from session (set during login using API)
    user = {
        "id": request.session.get("member_id"),
        "name": request.session.get("member_name"),
        "role": request.session.get("member_role"),
    }

    club = get_object_or_404(Clubs, id=club_id)
    role = get_role(request, club)  # this role is changed from models to api(request.session)

    context = {"club": club, "user": user, "role": role}
    return render(request, "individual_club.html", context)


def budget_request(request):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)
    club_id = request.session.get('club_id')
    club = get_object_or_404(Clubs, id=club_id)

    # ---- Role Restriction ----
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.INSTRUCTOR, Users.Role.STUDENT, Users.Role.ADMIN]:
        messages.error(request, "You are not allowed to access this page")
        return redirect('club_detail', club_id=club_id)

    # ! retrieve selected club from session
    if not club_id:
        messages.error(request, "No club selected")
        return redirect(reverse('home') + '#section_3')
    
    # if activity coordinator: view budget request review page
    if user.role in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.ADMIN]:

        if request.method == "POST":
            req_id = request.POST.get("request_id")
            new_status = request.POST.get("status")
            if req_id and new_status in [
                str(BudgetRequest.Status.PENDING),
                str(BudgetRequest.Status.APPROVED),
                str(BudgetRequest.Status.REJECTED)
            ]:
                req = get_object_or_404(BudgetRequest, id=req_id, club=club)
                req.status = int(new_status)
                req.save()
                messages.success(request, "Request updated successfully")
                return redirect("budget_request")

        budget_request = BudgetRequest.objects.filter(club=club)
        pending_count = budget_request.filter(status=BudgetRequest.Status.PENDING).count()
        approved_count = budget_request.filter(status=BudgetRequest.Status.APPROVED).count()
        rejected_count = budget_request.filter(status=BudgetRequest.Status.REJECTED).count()

        return render(request, "budget_request_review.html", {
            "club": club,
            "user": user,
            "budget_request": budget_request,
            "pending_count": pending_count,
            "approved_count": approved_count,
            "rejected_count": rejected_count,
        })


    
     # Instructor/Adviser: submit budget request page
    if request.method == "POST":
        title = request.POST.get("title")
        purpose = request.POST.get("purpose")
        amount = request.POST.get("amount")
        amount_words = request.POST.get("amount_words")
        requester = user.name  # instructor name

        if not purpose or not amount:
            messages.error(request, "Purpose and Amount are required")
            return render(request, 'budget_request.html', {"club": club, "user": user})

        BudgetRequest.objects.create(
            title=title,
            purpose=purpose,
            requester=requester,
            amount=amount,
            amount_words=amount_words,
            status=BudgetRequest.Status.PENDING,
            club=club,
        )

        messages.success(request, "Budget request submitted successfully")
        # return redirect("individual_club")
        return redirect('club_detail', club_id=club.id)
        
    budget_request = BudgetRequest.objects.filter(club=club)

    return render(request, 'budget_request.html', {
        "club": club, 
        "user": user,
        "budget_request": budget_request
        }) # go to budget_request (instructor page only)

# individual club
def election_club(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    role = get_role(request, club)
    context = {'club': club, 'user': user, 'role': role}
    return render(request, 'election_club.html', context)

# individual club
def get_club_achievement(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)
    club = get_object_or_404(Clubs, id=club_id)
    achievements = Achievement.objects.all().order_by('-date_posted')
    role = get_role(request, club)
    context = {
        'club': club,
        'user': user,
        'achievements': achievements,
        'role': role
    }
    return render(request, 'club-achievement.html', context)

def get_club_applicants(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = get_object_or_404(Clubs, id=club_id)
    applicants = MemberApplication.objects.filter(club=club, status=MemberApplication.Status.PENDING)
    role  = get_role(request, club)
    context = {'club': club, 'applicants': applicants, 'user': user, 'role': role}
    return render(request, 'approve_member.html', context)

# create event view ------------------------------------
# una gawa ka ng function (def) para sa event, i return mo yung .html file na gusto mong buksan kapag pinindot mo yung tag. 
#   Hindi mo na kelangan gamitin full path kasi naka register sa settings.py na base path ang /templates


# create event inside individual_club
def create_event(request, club_id):
    member_id = request.session.get("member_id")
    if not member_id:
        messages.error(request, "You must be logged in to create announcements")
        return redirect("home")

    club = get_object_or_404(Clubs, id=club_id)

    if request.method == "POST":
        name = request.POST.get("title")
        category = request.POST.get("category")
        content = request.POST.get("content")
        start_date = request.POST.get("announcementDate")
        end_date = request.POST.get("expiryDate") or None
        image = request.FILES.get("imageUpload")

        Announcement.objects.create(
            name=name,
            club=club,
            category=category,
            content=content,
            start_date=start_date,
            end_date=end_date,
            image=image
        )
        return redirect("create_event", club_id=club.id)

    announcements = Announcement.objects.filter(club=club)
    return render(request, "create_event.html", {
        "announcements": announcements,
        "club": club
    })



def get_role(request, club):
    user_id = request.session.get("member_id")
    user_role = request.session.get("member_role")

    if not user_id or user_role is None:
        return "Visitor"

    if user_role == Users.Role.ADMIN:
        return "Admin"
    elif user_role == Users.Role.ACTIVITY_COORDINATOR:
        return "Activity Coordinator"

    membership = Memberships.objects.filter(student_id=user_id, club=club).first()
    if membership:
        return membership.get_role_display()

    if Clubs.objects.filter(adviser_id=user_id, id=club.id).exists():
        return "Adviser"

    return "Visitor"
