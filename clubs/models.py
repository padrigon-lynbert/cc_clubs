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
    club_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Branch, on_delete=models.CASCADE, default=get_default_branch)
    description = models.TextField(max_length=255, null=True)
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
    banner = models.ImageField(upload_to='club_applications/banners/', null=True)
    submitted_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_submitted = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True, help_text='Enter a description about this club')
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
