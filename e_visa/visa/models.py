from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Userregistration(models.Model):
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def __str__(self):
        return self.username


    def __str__(self):
        return self.username


class VisaApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20)
    country_of_origin = models.CharField(max_length=100)
    purpose_of_visit = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'{self.user.username} - {self.passport_number} - {self.status}'
