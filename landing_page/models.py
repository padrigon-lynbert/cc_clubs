from django.db import models

# use accounts (used for login)
class Students(models.Model):
    acc_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'