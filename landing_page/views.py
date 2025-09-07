from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from .models import Users
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from individual_club.models import BudgetRequest, Users, Clubs

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

    user = Users.objects.filter(id=member_id) if member_id else None


    return render(request, 'landing_page.html', {
        "pending_budget_request": pending_budget_request,
        "user": user,
        "club_i_am_instructor": club_i_am_instructor})

def bridge(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'visit': return render(request, 'individual_club.html')
        elif action == 'club_directory': return render(request, 'club_directory.html')

    return render(request, 'landing_page.html')

# login and logout session, structured like this so we can edith redirect path fast
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

def logout(request):
    request.session.flush()
    return redirect('home')

def global_announcements(request):
    return render(request, 'global_announcement.html')

def global_chat(request):
    return render(request, 'global_chat.html')