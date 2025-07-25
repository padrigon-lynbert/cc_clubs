from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Students
from django.contrib import messages

# Create your views here.
def terms_and_conditions(request):
    if request.method == 'POST':
        if request.POST.get('agree') == 'on': return redirect('home')

    return render(request, 'terms.html')

def home(request):
    return render(request, 'landing_page.html')

def bridge(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'visit': return render(request, 'individual_club/individual_club.html')
        elif action == 'club_directory': return render(request, 'club_directory.html')

    return render(request, 'landing_page.html')

# login and logout session, structured like this so we can edith redirect path fast
def login_from_landing(request):
    if request.method == 'POST':
        acc_no = request.POST.get('member-login-number')
        password = request.POST.get('member-login-password')

        try:
            member = Students.objects.get(acc_no=acc_no, password=password)
            request.session['member_logged_in'] = True
            request.session['member_id'] = member.id
            request.session['member_name'] = member.name
            messages.success(request, 'Login successful')
            return redirect('home')
        except Students.DoesNotExist:
            messages.error(request, 'Invalid account or password')
            return redirect('home')

    return redirect('home')

def logout(request):
    request.session.flush()
    return redirect('home')


def register_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')
    return render(request, 'register/register_club.html')

def apply_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')
    return render(request, 'register/apply_club.html')

