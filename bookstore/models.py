from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class books(models.Model):
	book_name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	about = models.TextField()

	def __str__(self):
		return self.title
