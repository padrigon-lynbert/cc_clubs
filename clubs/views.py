from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClubRegistrationForm
from django.db import IntegrityError
from .models import Students, Clubs


# Create your views here.


def post_registration_club(request):
    # Login status checker
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')
    
    # Handle user submission
    if request.method == 'POST':
        form = ClubRegistrationForm(request.POST)
        if form.is_valid():
            club_name = form.cleaned_data['club_name'].strip().lower()

            # Check if the club is already officially registered
            if Clubs.objects.filter(club_name__iexact=club_name).exists():
                messages.error(request, 'This club is already registered. Please choose a different name.')
                return redirect('register_club')

            new_club_registration = form.save(commit=False)
            student_id = request.session.get('member_id')
            # Save user form
            try:
                student = Students.objects.get(id=student_id)
                new_club_registration.submitted_by = student
                new_club_registration.save()
                messages.success(request, 'Successfully submitted a club registration form.')
                return redirect('register_club')
            except IntegrityError:
                messages.error(request, 'The club name is already applied, try a different name.')
                return redirect('register_club')
        else:
            messages.error(request, 'The club name is already applied, try a different name.')
    else:
        form = ClubRegistrationForm()
    # Render the form
    context = {'form': form}
    return render(request, 'register/register_club.html', context)
