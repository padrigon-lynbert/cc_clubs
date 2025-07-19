from django.shortcuts import render

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

def individual_club(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'visit':
            return render(request, 'individual_club/individual_club.html')
    return render(request, 'landing_page.html')

def register_club(request):
    return render(request, 'register/register_club.html')

