from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import models

@python_2_unicode_compatible
class Author(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.EmailField(max_length=100, blank=False)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Post(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField('Date Published')

	def __str__(self):
		return self.title