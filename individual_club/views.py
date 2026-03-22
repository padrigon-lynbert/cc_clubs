from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError, transaction
from django.http import HttpResponseNotAllowed, JsonResponse
from clubs.models import Clubs, MemberApplication, Memberships, Achievement
from landing_page.models import Users
from .models import BudgetRequest, Link
from .forms import MembershipApplicationForm, AchievementForm
from clubs.models import Announcement
import base64, os
from datetime import datetime
from google import genai
from google.genai import types
from dotenv import load_dotenv

def submit_membership_application(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, acc_no=member_id)
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

    context = {'form': form, 'club': club, 'user': user}
    
    return render(request, 'register/apply_club.html', context)

def accept_membership_application(request, application_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
        
    user = get_object_or_404(Users, acc_no=member_id)
    # ---- Role Restriction ----
    user = get_object_or_404(Users, acc_no=member_id)
    if not Memberships.objects.filter(student=user, is_officer=True):
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
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in")
        return redirect('home')

    user = get_object_or_404(Users, acc_no=member_id)
    if user.role not in [Users.Role.OFFICER, Users.Role.ADVISER, Users.Role.ACTIVITY_COORDINATOR]:
        messages.error(request, "You are not allowed to reject applications")
        return redirect('home')

    member_application = get_object_or_404(MemberApplication, id=application_id)
    rejection_reason = request.POST.get('rejection_reason', '').strip()

    try:
        with transaction.atomic():
            member_application.status = MemberApplication.Status.REJECTED
            member_application.rejection_reason = rejection_reason
            member_application.save()
            messages.success(
                request,
                f"Rejected {member_application.student.name}'s application"
                + (f": {rejection_reason}" if rejection_reason else "")
            )
    except Exception as e:
        messages.error(request, f"Error rejecting application: {str(e)}")

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
    club = get_object_or_404(Clubs, id=club_id)

    member_id = request.session.get('member_id')
    is_member = False
    has_pending_application = False

    if member_id:
        user = get_object_or_404(Users, acc_no=member_id)

        is_member = Memberships.objects.filter(
            student=user,
            club=club
        ).exists()

        has_pending_application = MemberApplication.objects.filter(
            student=user,
            club=club,
            status=MemberApplication.Status.PENDING
        ).exists()

        total_members = Memberships.objects.filter(id=club_id).count()

    context = {
        "club": club,
        "is_member": is_member,
        "has_pending_application": has_pending_application,
        "total_members": total_members,
    }

    return render(request, "individual_club.html", context)


def budget_request(request):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, acc_no=member_id)
    club_id = request.session.get('club_id')
    club = get_object_or_404(Clubs, id=club_id)

    # ---- Role Restriction ---- // update
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.ADVISER, Users.Role.STUDENT, Users.Role.ADMIN]:
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
            reject_reason = request.POST.get("reject_reason")

            if req_id and new_status in [
                str(BudgetRequest.Status.PENDING),
                str(BudgetRequest.Status.APPROVED),
                str(BudgetRequest.Status.REJECTED)
            ]:

                req = get_object_or_404(BudgetRequest, id=req_id, club=club)

                new_status = int(new_status)

                # If rejecting, require reason
                if new_status == BudgetRequest.Status.REJECTED:
                    if not reject_reason:
                        messages.error(request, "Reject reason is required.")
                        return redirect("budget_request")

                    req.reject_reason = reject_reason

                else:
                    # Clear reason if approving
                    req.reject_reason = None

                req.status = new_status
                req.save()

                messages.success(request, "Request updated successfully")
                return redirect("budget_request")


        budget_request = BudgetRequest.objects.filter(club=club).order_by('status', '-created_at')

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
    
    user = get_object_or_404(Users, acc_no=member_id)

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

    user = Users.objects.get(acc_no=member_id)
    club = get_object_or_404(Clubs, id=club_id)
    achievements = Achievement.objects.filter(club=club).order_by('-date_posted')
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
    
    user = get_object_or_404(Users, acc_no=member_id)
    club = get_object_or_404(Clubs, id=club_id)

    # All applications for this club
    applicants = MemberApplication.objects.filter(club=club)

    # Counts for cards
    pending_count = applicants.filter(status=MemberApplication.Status.PENDING).count()
    approved_count = applicants.filter(status=MemberApplication.Status.APPROVED).count()
    rejected_count = applicants.filter(status=MemberApplication.Status.REJECTED).count()
    total_count = applicants.count()

    role = get_role(request, club)

    context = {
        'club': club,
        'applicants': applicants,
        'user': user,
        'role': role,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
        'total_count': total_count
    }

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

        # dates (parse from string -> date)
        start_date_str = request.POST.get("announcementDate")
        end_date_str = request.POST.get("expiryDate")

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None

        # category to int
        category = int(category) if category else Announcement.Category.GENERAL_ANNOUNCEMENT

        # handle image as bytes
        image_file = request.FILES.get("imageUpload")
        image_bytes = image_file.read() if image_file else None

        Announcement.objects.create(
            name=name,
            club=club,
            category=category,
            content=content,
            start_date=start_date,
            end_date=end_date,
            image=image_bytes,
        )
        return redirect("create_event", club_id=club.id)

    # render announcements with base64 images
    announcements = Announcement.objects.filter(club=club)
    for a in announcements:
        a.image_base64 = base64.b64encode(a.image).decode("utf-8") if a.image else None

    return render(request, "create_event.html", {
        "announcements": announcements,
        "club": club
    })

# deleting announcement inside create annoucement page
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.delete()
    messages.success(request, "Announcement deleted.")
    return redirect(request.META.get("HTTP_REFERER", "home"))

def display_link(request, club_id):
    club = get_object_or_404(Clubs, id=club_id)
    links = Link.objects.filter(club=club_id)
    context = {
        'links': links,
        'club': club,
        'club_id': club_id
    }
    return render(request, 'links.html', context)

def add_link(request, club_id):
    club = get_object_or_404(Clubs, id=club_id)
    
    if request.method == 'POST':
        url = request.POST.get('url')
        platform = request.POST.get('platform')
        
        if url and platform is not None:
            Link.objects.create(
                url=url,
                platform=int(platform),
                club_id=club_id
            )
            return redirect('display_link', club_id=club_id)
    
    context = {
        'club': club,
        'club_id': club_id,
        'platforms': Link.Platform.choices
    }
    return render(request, 'add_link.html', context)

def edit_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    
    if request.method == 'POST':
        url = request.POST.get('url')
        platform = request.POST.get('platform')
        
        if url and platform is not None:
            link.url = url
            link.platform = int(platform)
            link.save()
            return redirect('display_link', club_id=link.club_id)
    
    context = {
        'link': link,
        'club_id': link.club_id,
        'platforms': Link.Platform.choices
    }
    return render(request, 'edit_link.html', context)

def delete_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    club_id = link.club_id
    
    if request.method == 'POST':
        link.delete()
        return redirect('display_link', club_id=club_id)
    
    context = {
        'link': link,
        'club_id': club_id
    }
    return render(request, 'delete_link.html', context)

def achievement_create(request, club_id):
    """Create a new achievement for a specific club"""
    club = get_object_or_404(Clubs, id=club_id)
    
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.club = club
            achievement.save()
            messages.success(request, 'Achievement created successfully!')
            return redirect('club_achievement', club_id=club.id)
    else:
        form = AchievementForm()
    
    context = {
        'form': form,
        'club': club,
        'action': 'Create',
    }
    return render(request, 'achievements/achievement_form.html', context)

def achievement_update(request, club_id, achievement_id):
    """Update an existing achievement"""
    club = get_object_or_404(Clubs, pk=club_id)
    achievement = get_object_or_404(Achievement, pk=achievement_id, club=club)
    
    if request.method == 'POST':
        # Include request.FILES to handle the image
        form = AchievementForm(request.POST, request.FILES, instance=achievement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Achievement updated successfully!')
            return redirect('club_achievement', club_id=club.id)
    else:
        form = AchievementForm(instance=achievement)
    
    context = {
        'form': form,
        'club': club,
        'achievement': achievement,
        'action': 'Update',
    }
    return render(request, 'achievements/achievement_form.html', context)



def achievement_delete(request, club_id, achievement_id):
    """Delete an achievement"""
    club = get_object_or_404(Clubs, pk=club_id)
    achievement = get_object_or_404(Achievement, pk=achievement_id, club=club)
    
    if request.method == 'POST':
        achievement.delete()
        messages.success(request, 'Achievement deleted successfully!')
        return redirect('club_achievement', club_id=club.id)
    
    context = {
        'club': club,
        'achievement': achievement,
    }
    return render(request, 'achievements/achievement_confirm_delete.html', context)

# supporting function to specify individual role inside individual dlub
def get_role(request, club):
    user_id = request.session.get("member_id")
    user_role = request.session.get("member_role")

    if not user_id or user_role is None:
        return "Visitor"

    if user_role == Users.Role.ADMIN:
        return "Admin"
    elif user_role == Users.Role.ADVISER:
        return "Adviser"
    elif user_role == Users.Role.STUDENT:
        return "Student"

    membership = Memberships.objects.filter(student_id=user_id, club=club).first()
    if membership:
        return membership.get_role_display()

    if Clubs.objects.filter(adviser_id=user_id, id=club.id).exists():
        return "Activity Coordinator"

    return "Visitor"

def analyze_club(request, club_id):
    club = Clubs.objects.get(id=club_id)
    achievements = Achievement.objects.filter(club=club)
    members = Memberships.objects.filter(club=club_id).count()
    achievement_data = list(achievements.values('title', 'details', 'club', 'date_posted'))
    pending, rejected, approved = [
                                    BudgetRequest.objects.filter(club=club, status=BudgetRequest.Status.PENDING).count(), 
                                    BudgetRequest.objects.filter(club=club, status=BudgetRequest.Status.REJECTED).count(),
                                    BudgetRequest.objects.filter(club=club, status=BudgetRequest.Status.APPROVED).count(),
                                ]

    information = {
        'name': club.club_name,
        'achievements': achievement_data,
        'member_count': members,
        'total_achievements': achievements.count(),
        'pending_budget_request': pending,
        'rejected_budget_request': rejected,
        'approved_budget_request': approved,
    }
    analyzed_data = generate_analysis(information)

    return JsonResponse({
        "analysis": analyzed_data
    })

def generate_analysis(club_info):
    load_dotenv()
    GEMINI_API_KEY = "AIzaSyBNI6xTvB4GrLZpEUlE40xN8yYl0hnyt2g"
    client = genai.Client(api_key=GEMINI_API_KEY)

    club_info_str = f"""
    Club Name: {club_info['name']}
    Member Count: {club_info['member_count']}
    Total Achievements: {club_info['total_achievements']}
    Achievements: {club_info['achievements']}
    Pending Budget Requests: {club_info['pending_budget_request']}
    Rejected Budget Requests: {club_info['rejected_budget_request']}
    Approved Budget Requests: {club_info['approved_budget_request']}
    """

    generation_config = types.GenerateContentConfig(
        max_output_tokens=1000,
        temperature=0.7
    )
    response = client.models.generate_content(
        model="gemma-3-27b-it",
        contents=f"Analyze this club performance data concisely in paragraph:\n\n{club_info_str}",
        config=generation_config,
    )
    return response.text;
