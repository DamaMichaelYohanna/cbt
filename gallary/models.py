from django.db import models
import os
from django.urls import reverse
choice = (('draft','draft'),('published','published'))

def get_image_path(instance, filename):
    return os.path.join('photo',str(instance.id),filename)

class Comments(models.Model):
    """docstring for ."""
    post = models.ForeignKey('Post',on_delete = models.CASCADE,
        related_name = 'comments')
    body = models.TextField(max_length=500)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now = True)

class Post(models.Model):
	post = models.TextField('Description',max_length = 1000)
	img = models.ImageField("",upload_to = get_image_path)
	category = models.CharField(choices = choice, default = choice[0],max_length = 50)
	date = models.DateTimeField(auto_now = True)
	class Meta:
		ordering = ('-date',)

	def get_absolute_url(self):
		return reverse('gallary:Details',self.img)

	def __str__(self):
		return '{}'.format(self.post)
