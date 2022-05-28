from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	size = models.CharField(max_length=50, blank=True, null=True)
	detail = models.TextField(null=True, blank=True)
	quantity = models.IntegerField(default=1)
	imagePath = models.ImageField(upload_to="medias", null=True, blank=True)

	def __str__(self):
		return self.name


 