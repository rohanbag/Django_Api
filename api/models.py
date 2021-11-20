from django.db import models

# Create your models here.
class Matl(models.Model):
	name = models.CharField(max_length=100) 
	price = models.IntegerField(max_length=20)
	company = models.CharField(max_length=50)
	qty = models.IntegerField(max_length=10)

	def __str__(self):
		return self.name