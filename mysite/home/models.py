from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(User):
    user = models.ForeignKey(User,related_name="customer_profile",on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class BdayClub():
    first_name = models.CharField(max_length=30,default="First Name")
    last_name = models.CharField(max_length=30,default="Last Name")
    email = models.CharField(max_length=50,default="Email")

class CaterEstimate():
    item = models.CharField(max_length=30,default="")
    total = models.PositiveIntegerField(default=0)


class Reservations():
    first_name = models.CharField(max_length=30,default="First Name")
    last_name = models.CharField(max_length=30,default="Last Name")
    phone_number = models.IntegerField(max_length=10,default="Phone Number")
    email = models.CharField(max_length=50,default="Email")
    party = models.CharField(max_length=1,default=0)
    requests = models.TextField(max_length=300,default="Special Requests")
