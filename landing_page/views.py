from django.shortcuts import render

# Create your views here.
def terms_and_conditions(request):
    return render(request, 'index.html')