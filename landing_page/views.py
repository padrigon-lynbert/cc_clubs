from django.shortcuts import render, redirect

# Create your views here.
def terms_and_conditions(request):
    return render(request, 'terms.html')

# def home(request):
#     if request.method == 'POST':
#         if request.POST.get('agree') == 'on':
#             return render(request, 'landing_page.html')
#     return render(request, 'terms.html')

def home(request):
    if request.method == 'POST':
        if request.POST.get('agree') == 'on':
            return render(request, 'landing_page.html')
    return render(request, 'terms.html')

def bridge(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'visit': return render(request, 'individual_club/individual_club.html')
        elif action == 'club_directory': return render(request, 'club_directory.html')

    return render(request, 'landing_page.html')

def register_club(request):
    return render(request, 'register/register_club.html')

def apply_club(request):
    return render(request, 'register/apply_club.html')

