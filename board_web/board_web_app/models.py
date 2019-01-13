from django.db import models


class trip(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	available_spots = models.IntegerField(default=1)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.title