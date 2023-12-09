from django.db import models

BOOL_CHOICES = ((True, 'Admin - can delete members'), (False, 'Regular - cannot delete members'))

# Create your models here.
class TeamMember(models.Model):
    objects = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False, choices=BOOL_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
