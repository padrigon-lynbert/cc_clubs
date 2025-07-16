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
