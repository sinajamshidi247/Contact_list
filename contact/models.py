from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    realation = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    email = models.EmailField()
    number =  PhoneField(blank=True, help_text='Contact phone number')
