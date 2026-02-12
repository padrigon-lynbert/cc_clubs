from django.db import models
from django.utils.translation import gettext_lazy as _
from clubs.models import Clubs
from landing_page.models import Users
from django.utils import timezone

# Create your models here.

class BudgetRequest(models.Model):
    title = models.CharField(max_length=255, default='Not Specified')
    purpose = models.CharField(max_length=255)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    requester = models.CharField(max_length=255)

    amount = models.CharField(max_length=20)  # (we'll improve this below)

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

    # ✅ NEW FIELD
    reject_reason = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "budget_request"

class Link(models.Model):
    url = models.URLField(max_length=200)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.get_platform_display()}: {self.url}"
