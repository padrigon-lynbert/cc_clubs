from django.db import models
from django.utils.translation import gettext_lazy as _
from clubs.models import Clubs
from landing_page.models import Users
from django.utils import timezone

# Create your models here.

class BudgetRequest(models.Model):
    title = models.CharField(max_length=255, default='Not Specified')  # just store name as text
    purpose = models.CharField(max_length=255)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    requester = models.CharField(max_length=255)  # just store name as text
    amount = models.CharField(max_length=20) # fuck this error decimal can't handle commas I'm storing this as text

    class Status(models.IntegerChoices):
        PENDING = 0, "Pending"
        APPROVED = 1, "Approved"
        REJECTED = 2, "Rejected"

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING,
    )

    amount_words = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "budget_request"

class Link(models.Model):
    url = models.URLField(max_length=200)
    club_id = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    class Platform(models.IntegerChoices):
        FACEBOOK = 0, "Facebook"
        TWITTER = 1, "Twitter/X"
        INSTAGRAM = 2, "Instagram"

    platform = models.IntegerField(
        choices=Platform.choices,
        default=Platform.FACEBOOK,
    )

    class Meta:
        db_table = 'link'
