from django.db import models
from django.utils.translation import gettext_lazy as _
from clubs.models import Clubs
from landing_page.models import Users
from django.utils import timezone

# Create your models here.

class BudgetRequest(models.Model):
    purpose = models.CharField(max_length=255)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    requester = models.CharField(max_length=255)  # just store name as text
    amount = models.DecimalField(max_digits=10, decimal_places=2)

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
