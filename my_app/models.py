from django.db import models

class Destination(models.Model):
	#id= models.IntegerField()
	name=models.CharField(max_length=100)
	img=models.ImageField(upload_to='images')


