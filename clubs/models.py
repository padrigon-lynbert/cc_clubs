from django.db import models
from django.utils.translation import gettext_lazy as _
from landing_page.models import Users

# Create your models here.

def get_default_branch():
    return Branch.objects.get_or_create(branch_name='Main Campus')[0].id

class Branch(models.Model):
    branch_name = models.CharField(max_length=30)

    def __str__(self):
        return self.branch_name
    
    class Meta:
        db_table = 'school_branch'

class Clubs(models.Model):
    club_name = models.CharField(max_length=255, unique=True)
    acronym = models.CharField(max_length=30, unique=True, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    chairperson = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='chaired_clubs', null=True, blank=True)
    adviser = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='advised_clubs', null=True, blank=True)
    year_level = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Branch, on_delete=models.CASCADE, default=get_default_branch)
    banner = models.ImageField(upload_to='club_applications/banners/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # accepting = models.BooleanField(default=False)
    # competing = models.BooleanField(default=False)

    def __str__(self):
        return self.club_name
    
    class Meta:
        db_table = 'clubs'


class Memberships(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    is_officer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.name} - {self.club.club_name}'
    
    class Meta:
        db_table = 'memberships'
        constraints = [
            models.UniqueConstraint(fields=['student', 'club'], name='unique_membership')
        ]

class MemberApplication(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    medical_form = models.ImageField(upload_to='membership_applications/medical_forms/', null=False)
    certificate_of_recognition = models.ImageField(upload_to='membership_applications/cor/', null=False)
    student_id_card = models.ImageField(upload_to='membership_applications/identification_cards/', null=False)
    date_submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.name} wants to apply to {self.club.club_name}'
    
    class Meta:
        db_table = 'member_application'
        ordering = ['-date_submitted']

class ClubApplication(models.Model):
    club_name = models.CharField(max_length=255, unique=True)
    acronym = models.CharField(max_length=30, null=True, unique=True, blank=True)
    adviser = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='application_adviser', null=True)
    banner = models.ImageField(upload_to='club_applications/banners/', null=True, blank=True)
    submitted_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='submitted_application', null=True, blank=True)
    year_level = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, help_text='Enter a description about this club')
    location = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Status(models.IntegerChoices):
        PENDING = 0, _('Pending')
        APPROVED = 1, _('Approved')
        REJECTED = 2, _('Rejected')

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name='Status',
    )

    def __str__(self):
        return f'{self.club_name} is proposed by {self.submitted_by.name}'
    
    class Meta:
        db_table = 'club_application'
        ordering = ['-date_submitted']
        verbose_name_plural = 'Club Applications'

class Event(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.club.club_name} Event - {self.name}'
    
    class Meta:
        db_table = 'events'

class BudgetRequest(models.Model):
    purpose = models.CharField(max_length=255, blank=False, null=False)
    details = models.CharField(max_length=255)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    class Status(models.IntegerChoices):
        PENDING = 0, _('Pending')
        APPROVED = 1, _('Approved')
        REJECTED = 2, _('Rejected')

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return f'{self.club.club_name} is requesting budget for {self.purpose}'
    
    class Meta:
        db_table = 'budget_requests'