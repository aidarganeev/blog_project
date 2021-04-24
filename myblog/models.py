from django.db import models

# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length=100)
	post_date = models.DateTimeField()
	post_text = models.CharField(max_length=500)
	post_image = models.ImageField(upload_to='post_images/')