from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from .models import Users
from django.contrib import messages
from django.db import connections
from django.urls import reverse
from individual_club.models import BudgetRequest, Users, Clubs
from clubs.models import Memberships
import requests
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
    club_i_am_instructor = Clubs.objects.filter(adviser=member_id) if member_id else None
    clubs_student_joined = Clubs.objects.filter(memberships__student_id=member_id) if member_id else None

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
        "role_display": role_display
    }


    return render(request, 'landing_page.html', context)

# def bridge(request):
#     if request.method == 'POST':
#         action = request.POST.get('action')

#         if action == 'visit': return render(request, 'individual_club.html')
#         elif action == 'club_directory': return render(request, 'club_directory.html')

#     return render(request, 'landing_page.html')

# This is our login using database (default or not using any api), uncomment for tests
# login and logout session, structured like this so we can edith redirect path fast
'''
def login_from_landing(request): 
    if request.method == 'POST':
        acc_no = request.POST.get('member-login-number')
        password = request.POST.get('member-login-password')

        try:
            member = Users.objects.get(acc_no=acc_no, password=password)
            request.session['member_logged_in'] = True
            request.session['member_id'] = member.id
            request.session['member_name'] = member.name
            messages.success(request, 'Login successful')
            return redirect('home')
        except Users.DoesNotExist:
            messages.error(request, 'Invalid account or password')
            return redirect('home')

    return redirect('home')
'''

# login using api
def login_from_landing(request):
    if request.method == 'POST':
        acc_no = request.POST.get('member-login-number')
        password = request.POST.get('member-login-password')

        # api localhost
        # url = "http://localhost/a_test_api/api_login.php"  # change to your PHP API URL

        # api live
        url = "https://cc-clubs-1.onrender.com/api_login.php"

        try:
            res = requests.post(url, json={"acc_no": acc_no, "password": password}, timeout=10)
            api_res = res.json()
        except Exception as e:
            messages.error(request, f"API error: {e}")
            return redirect('home')

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
    
    return redirect('home')


def logout(request):
    request.session.flush()
    connections.close_all() # drop all db connection from this session immediately
    return redirect('home')

def global_announcements(request):
    return render(request, 'global_announcement.html')

def profile_settings(request):
    return render(request, 'profile_settings.html')
