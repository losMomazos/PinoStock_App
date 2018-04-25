from django.db import models

# Create your models here.
class Gpu(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Cpu(model.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name


class MotherBoard(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	socket = models.CharField(max_length=50)
	def __str__(self):
		return self.name
