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
from django.shortcuts import redirect
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

from individual_club.views import get_role

# Create your views here.

# termporary bypass input in low tier browsers
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




@csrf_exempt
def login_from_landing(request):
    if request.method != 'POST':
        return redirect('login_page')

    email = request.POST.get('member-login-email', '').strip()
    password = request.POST.get('member-login-password', '').strip()

    # ---- limiter ----
    MAX_ATTEMPTS = 4
    LOCK_TIME = 15 * 60  # seconds

    key = f"login_attempts_{email}"
    attempts = cache.get(key, 0)

    if attempts >= MAX_ATTEMPTS:
        messages.error(request, "Too many attempts. Try again later.")
        return redirect('login_page')

    # ---- auth APIs ----
    apis = [
        "https://cc-clubs-1.onrender.com/endpoint_fms.php",
        "https://cc-clubs-1.onrender.com/endpoint_rms.php"
    ]

    user_data = None

    for url in apis:
        try:
            res = requests.post(
                url,
                json={"email": email, "password": password},
                timeout=10
            )
            api_res = res.json()
            if api_res.get("status") == "success":
                user_data = api_res.get("user")
                break
        except Exception:
            pass

    # ---- success ----
    if user_data:
        cache.delete(key)  # reset limiter

        request.session['member_logged_in'] = True
        request.session['member_id'] = user_data.get("id")
        request.session['member_role'] = user_data.get("role")

        messages.success(request, "Login successful")
        return redirect('home')

    # ---- failure ----
    cache.set(key, attempts + 1, LOCK_TIME)
    messages.error(request, "Invalid account or password")
    return redirect('login_page')


# login no limiter
'''
def login_from_landing(request):
    if request.method != 'POST':
        return redirect('login_page')

    email = request.POST.get('member-login-email', '').strip()
    password = request.POST.get('member-login-password', '').strip()

    apis = [
        "https://cc-clubs-1.onrender.com/endpoint_fms.php",  # hashed
        "https://cc-clubs-1.onrender.com/endpoint_rms.php"   # hashed
    ]

    user_data = None

    for url in apis:
        try:
            # Send exactly what you type in Postman
            res = requests.post(url, json={"email": email, "password": password}, timeout=10)
            api_res = res.json()
            if api_res.get("status") == "success":
                user_data = api_res.get("user")
                break
        except Exception:
            continue

    if user_data:

        user, created = Users.objects.update_or_create(
        acc_no=user_data.get("id"),  # or email / account number
        defaults={
            "name": f"{user_data.get('first_name')} {user_data.get('last_name')}",
            "role": map_api_role(user_data.get("role")),
            }
        )

        request.session['member_logged_in'] = True
        request.session['member_id'] = user_data.get("id")
        request.session['first_name'] = user_data.get("first_name")
        request.session['middle_name'] = user_data.get("middle_name")
        request.session['last_name'] = user_data.get("last_name")
        request.session['member_role'] = user_data.get("role")
        request.session['department'] = user_data.get("department")
        messages.success(request, 'Login successful')

        Users.objects.update_or_create(acc_no=request.session['member_id'], )
        return redirect('home')
    else:
        messages.error(request, 'Invalid account or password')
        return redirect('login_page')
'''

# test for tracing
'''
from django.http import JsonResponse
@csrf_exempt
def login_from_landing(request):
    if request.method != 'POST':
        return JsonResponse({"error": "not post"})

    email = request.POST.get('member-login-email', '').strip()
    password = request.POST.get('member-login-password', '').strip()

    apis = [
        "https://cc-clubs-1.onrender.com/endpoint_fms.php",
        "https://cc-clubs-1.onrender.com/endpoint_rms.php"
    ]

    user_data = None

    for url in apis:
        try:
            res = requests.post(url, json={"email": email, "password": password}, timeout=10)
            api_res = res.json()
            if api_res.get("status") == "success":
                user_data = api_res.get("user")
                break
        except Exception:
            continue

    return JsonResponse({
        "email": email,
        "password": password,
        "api_user_data": user_data,
    })

# tracer
@csrf_exempt
def debug_login(request):
    if request.method != 'POST':
        return JsonResponse({"error": "not post"})

    # get POST data from form
    email = request.POST.get('member-login-email', '').strip()
    password = request.POST.get('member-login-password', '').strip()

    # APIs to call
    apis = [
        "https://cc-clubs-1.onrender.com/endpoint_fms.php",
        "https://cc-clubs-1.onrender.com/endpoint_rms.php"
    ]

    user_data = None

    # try each API until success
    for url in apis:
        try:
            res = requests.post(url, json={"email": email, "password": password}, timeout=10)
            api_res = res.json()
            if api_res.get("status") == "success":
                user_data = api_res.get("user")
                break
        except Exception:
            continue

    # return JSON exactly like original login
    return JsonResponse({
        "email": email,
        "password": password,
        "api_user_data": user_data,
    })

'''



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

def map_api_role(api_role: str) -> int:
    role = (api_role or "").strip().lower()

    if role in ["Student"]:
        return Users.Role.STUDENT

    if role in ["professor"]:
        return Users.Role.ADVISER

    if role in ["coordinator"]:
        return Users.Role.ACTIVITY_COORDINATOR

    return Users.Role.STUDENT  # safe default