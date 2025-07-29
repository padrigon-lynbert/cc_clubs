from django.db import models
from django.utils.translation import gettext_lazy as _

# use accounts (used for login)
class Students(models.Model):
    acc_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'

class Clubs(models.Model):
    club_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.club_name


class Memberships(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
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

class ClubApplication(models.Model):
    club_name = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_submitted = models.DateField(auto_now_add=True)
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
