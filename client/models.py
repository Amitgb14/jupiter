# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

STATUS_CHOICES = ((1, 'Yes'),(0, 'No'),)

class Country(models.Model):
    country_name = models.CharField("Country", max_length=20, blank=False)
    status = models.BooleanField("Status", default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}".format(self.country_name)


class State(models.Model):
    country = models.ForeignKey(Country)
    state_name = models.CharField("State", max_length=20, blank=False)
    status = models.BooleanField("Status", default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}".format(self.state_name)


class City(models.Model):
    state = models.ForeignKey(State)
    city_name = models.CharField("City", max_length=20, blank=False)
    status = models.BooleanField("Status", default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}".format(self.city_name)


class User(AbstractUser):
    # user = models.OneToOneField(User, related_name="user_info", on_delete=models.CASCADE)
    # first_name = models.CharField("First Name", max_length=200, blank=False)
    # last_name = models.CharField("Last Name", max_length=200, blank=False)
    # email_id = models.EmailField("Email id", blank=False, unique=True)
    address_line1 = models.CharField("Address Line 1", max_length=200, blank=True)
    address_line2 = models.CharField("Address Line 2", max_length=200, blank=True)
    city = models.ForeignKey(City, blank=True, null=True)
    state = models.ForeignKey(State, blank=True, null=True)
    postal_code = models.CharField("Postal Code", max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
    contact_no = models.CharField("Contact Numer", max_length=15, blank=True, unique=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "Done" # {} {}".format(self.first_name, self.last_name)

class Message(models.Model):
    user = models.ForeignKey(User, null=True, related_name="user_message")
    message = models.TextField("Message")
    read = models.BooleanField('Read', default=0, choices=STATUS_CHOICES, blank=False)
    date = models.DateTimeField("Date", default=timezone.now, blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}".format(self.user)
