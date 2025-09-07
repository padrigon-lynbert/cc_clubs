from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from clubs.models import Clubs, MemberApplication, Achievement
from landing_page.models import Users
from .models import BudgetRequest


def post_membership_application(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')
    return render(request, 'register/apply_club.html')

def member_list(request):
    return render(request, 'member_list.html')

def individual_club(request):
    if not request.session.get('member_logged_in'):
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    if request.method == "POST":
        club_id = request.POST.get("club_id")

        if not club_id:  # nothing selected
            return redirect(reverse('home') + '#section_3')

        # store selected club
        request.session['club_id'] = club_id

        # redirect to clean URL with ID
        return redirect('club_detail', club_id=club_id)

    # if someone goes here directly without POST
    return redirect(reverse('home') + '#section_3')

# for individual club to carry id in the url
def club_detail(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    context = {'club': club, 'user': user}
    return render(request, 'individual_club.html', context)



def budget_request(request):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)
    club_id = request.session.get('club_id')
    club = get_object_or_404(Clubs, id=club_id)

    # ---- Role Restriction ----
    if user.role not in [Users.Role.ACTIVITY_COORDINATOR, Users.Role.INSTRUCTOR]:
        messages.error(request, "You are not allowed to access this page")
        return render(request, 'individual_club.html', {"club": club})

    # ! retrieve selected club from session
    if not club_id:
        messages.error(request, "No club selected")
        return redirect(reverse('home') + '#section_3')
    
    # if activity coordinator: view budget request review page
    if user.role == Users.Role.ACTIVITY_COORDINATOR:

        if request.method == "POST":
            req_id = request.POST.get("request_id")
            new_status = request.POST.get("status")
            if req_id and new_status in [
                str(BudgetRequest.Status.PENDING),
                str(BudgetRequest.Status.APPROVED),
                str(BudgetRequest.Status.REJECTED)
            ]:
                req = get_object_or_404(BudgetRequest, id=req_id, club=club)
                req.status = int(new_status)
                req.save()
                messages.success(request, "Request updated successfully")
                return redirect("budget_request")

        budget_request = BudgetRequest.objects.filter(club=club)
        pending_count = budget_request.filter(status=BudgetRequest.Status.PENDING).count()
        approved_count = budget_request.filter(status=BudgetRequest.Status.APPROVED).count()
        rejected_count = budget_request.filter(status=BudgetRequest.Status.REJECTED).count()

        return render(request, "budget_request_review.html", {
            "club": club,
            "user": user,
            "budget_request": budget_request,
            "pending_count": pending_count,
            "approved_count": approved_count,
            "rejected_count": rejected_count,
        })


    
     # Instructor/Adviser: submit budget request page
    if request.method == "POST":
        title = request.POST.get("title")
        purpose = request.POST.get("purpose")
        amount = request.POST.get("amount")
        amount_words = request.POST.get("amount_words")
        requester = user.name  # instructor name

        if not purpose or not amount:
            messages.error(request, "Purpose and Amount are required")
            return render(request, 'budget_request.html', {"club": club, "user": user})

        BudgetRequest.objects.create(
            title=title,
            purpose=purpose,
            requester=requester,
            amount=amount,
            amount_words=amount_words,
            status=BudgetRequest.Status.PENDING,
            club=club,
        )

        messages.success(request, "Budget request submitted successfully")
        # return redirect("individual_club")
        return redirect('club_detail', club_id=club.id)
        
    budget_request = BudgetRequest.objects.filter(club=club)

    return render(request, 'budget_request.html', {
        "club": club, 
        "user": user,
        "budget_request": budget_request
        }) # go to budget_request (instructor page only)


def election_club(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    context = {'club': club, 'user': user}
    return render(request, 'election_club.html', context)

    
def get_club_achievement(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')

    user = get_object_or_404(Users, id=member_id)
    club = get_object_or_404(Clubs, id=club_id)
    achievements = Achievement.objects.all().order_by('-date_posted')

    context = {
        'club': club,
        'user': user,
        'achievements': achievements,
    }
    return render(request, 'club-achievement.html', context)

def get_club_applicants(request, club_id):
    member_id = request.session.get('member_id')
    if not member_id:
        messages.error(request, "You must be logged in to access this page")
        return redirect(reverse('home') + '#section_3')
    
    user = get_object_or_404(Users, id=member_id)
    club = Clubs.objects.get(id=club_id)
    applicant = MemberApplication.objects.filter(club=club)
    context = {'club': club, 'applicant': applicant, 'user': user}
    return render(request, 'approve_member.html', context)

# create event view ------------------------------------
# una gawa ka ng function (def) para sa event, i return mo yung .html file na gusto mong buksan kapag pinindot mo yung tag. 
#   Hindi mo na kelangan gamitin full path kasi naka register sa settings.py na base path ang /templates

def create_event(request):
    
    # kapag pinindot mo ito yung page na pupuntahan(.html sa return), para malaman ng system kung anong url ang gagamitin mo kelangan mo i define,
        #kaya pupunta ka sa urls ng application na ito (folder na may views.py), open mo urls.py same folder
    return render(request, 'create_event.html')