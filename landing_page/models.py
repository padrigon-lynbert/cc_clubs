from django.db import models
from django.utils.translation import gettext_lazy as _

# use accounts (used for login)
class Users(models.Model):
    acc_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    class Role(models.IntegerChoices):
        STUDENT = 0, _('Student')
        INSTRUCTOR = 1, _('Instructor')
        ACTIVITY_COORDINATOR = 2, _('Coordinator')
        ADMIN = 3, _('Admin')

    role = models.IntegerField(
        choices=Role.choices,
        default=Role.STUDENT # Remove this after testing
    )
    def __str__(self):
        return f'{self.name} - {self.get_role_display()}' 

    class Meta:
        db_table = 'users'