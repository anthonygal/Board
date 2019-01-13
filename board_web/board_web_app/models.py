from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Trip(models.Model):
	organiser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	title = models.CharField(max_length=200)
	description = models.TextField()
	available_spots = models.IntegerField(default=1)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.title

class CustomUser(AbstractUser):
	# add additional fields in here
	rating = models.IntegerField(default=None, null=True)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	def __str__(self):
		return self.email