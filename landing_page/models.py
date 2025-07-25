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

class Clubs(models.Model):
    club_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.club_name} - Established: {self.created_at}'


class Memberships(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    is_officer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.name} - {self.club.club_name}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'club'], name='unique_membership')
        ]