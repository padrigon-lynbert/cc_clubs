from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from .models import Users
from django.contrib import messages
from django.db import connections
from django.db.models import Q
from django.urls import reverse
from individual_club.models import BudgetRequest, Users, Clubs
from clubs.models import Announcement, ClubApplication
import base64, requests

from individual_club.views import get_role

# Create your views here.

# termporary bypass input in low tier browsers
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def terms_and_conditions(request):
    if request.method == 'POST' and request.POST.get('agree') == 'on':
        return redirect('home')
    return render(request, 'terms.html')

def home(request):
    pending_budget_request = BudgetRequest.objects.filter(status=0)
    member_id = request.session.get('member_id')
    from django.db.models import Q

    club_applications = ClubApplication.objects.filter(Q(status=ClubApplication.Status.REJECTED) | Q(status=ClubApplication.Status.APPROVED), submitted_by=member_id) if member_id else None

    club_i_am_instructor = Clubs.objects.filter(adviser=member_id) if member_id else None
    clubs_student_joined = Clubs.objects.filter(memberships__student_id=member_id) if member_id else None
    recent_announcements = Announcement.objects.order_by('-announcement_date')[:2]

    for a in recent_announcements:
        if a.image:
            a.image_base64 = base64.b64encode(a.image).decode()
        else:
            a.image_base64 = None


     # add role to each club object
    clubs_with_roles = []
    if clubs_student_joined:
        for club in clubs_student_joined:
            club.role = get_role(request, club)
            clubs_with_roles.append(club)

    user_role_value = request.session.get("member_role")
    role_display = dict(Users.Role.choices).get(user_role_value, "Guest")
    
    context = {
        "pending_budget_request": pending_budget_request,
        "club_i_am_instructor": club_i_am_instructor,
        "club_student_joined": clubs_with_roles,
        "role_display": role_display,
        "recent_announcements": recent_announcements,
        "club_applications": club_applications
    }

    return render(request, 'landing_page.html', context)

'''
# login using api
def login_from_landing(request):

    if request.method == 'POST':
        email = request.POST.get('member-login-email')
        password = request.POST.get('member-login-password')

        # api live
        url = "https://cc-clubs-1.onrender.com/api_login.php"

        try:
            res = requests.post(url, json={"email": email, "password": password}, timeout=10)
            api_res = res.json()
        except Exception as e:
            messages.error(request, f"API error: API took too long to respond")
            return redirect('login_page')

        if api_res.get("status") == "success":
            user = api_res.get("user", {})
            request.session['member_logged_in'] = True
            request.session['member_id'] = user.get("id")
            request.session['member_name'] = user.get("name")
            request.session['member_role'] = user.get("role")
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid account or password')
    
    return redirect('login_page')
'''

# login using api
def login_from_landing(request):

    if request.method == 'POST':
        email = request.POST.get('member-login-email')
        password = request.POST.get('member-login-password')

        # api live
        url = "https://cc-clubs-1.onrender.com/endpoint_fms.php"

        try:
            res = requests.post(url, json={"email": email, "password": password}, timeout=10)
            api_res = res.json()
        except Exception as e:
            messages.error(request, f"API error: API took too long to respond")
            return redirect('login_page')

        if api_res.get("status") == "success":
            user = api_res.get("user", {})
            request.session['member_logged_in'] = True
            request.session['member_id'] = user.get("id")
            request.session['member_name'] = user.get("name")
            request.session['member_role'] = user.get("role")
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid account or password')
    
    return redirect('login_page')


def logout(request):
    request.session.flush()
    connections.close_all() # drop all db connection from this session immediately
    return redirect('home')

from clubs.models import Announcement

def global_announcements(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    announcements = Announcement.objects.all().order_by('-announcement_date')
    for a in announcements:
        if a.image:
            a.image_base64 = base64.b64encode(a.image).decode("utf-8")
        else:
            a.image_base64 = None
    return render(request, 'global_announcement.html', {
        "announcements": announcements
    })

def profile_settings(request):
    return render(request, 'profile_settings.html')

def login_page(request):
    if request.session.get('member_logged_in'):
        messages.error(request, "You are already logged in.")
        return redirect('home')  
    return render(request, 'login.html')


def upcoming_events(request):
    return render(request, 'upcoming_events.html')