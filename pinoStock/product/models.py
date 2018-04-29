from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=255)
	code = models.IntegerField(default=1)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ('id',)

class Gpu(models.Model):
	name = models.CharField(max_length=60)
	patentGPU = models.CharField(max_length=50)
	baseCloack = models.FloatField(null = False,default=0.0)
	memoryCloack = models.FloatField(null = False,default=0.0)
	busSupport = models.CharField(max_length=30)
	memoryInterface = models.CharField(max_length=20)
	maximumDigitalResolution = models.CharField(max_length=30)
	recomendedSystemPower = models.FloatField(null = False,default=0.0)
	maximumTemperature = models.FloatField(null = False,default=0.0)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Cpu(models.Model):
	name = models.CharField(max_length=60)
	patentCPU = models.CharField(max_length=50)
	baseFrequency = models.FloatField(null = False,default=0.0)
	maxFrequency = models.FloatField(null = False,default=0.0)
	numberOfCores = models.IntegerField(null = False,default=1)
	numberOfThreads = models.IntegerField(null = False,default=1)
	socket = models.CharField(max_length=50)
	cache = models.IntegerField(null=False,default=0)
	maxTemperature = models.FloatField(null = False,default=0.0)
	TDP = models.FloatField(null=False,default=0.0)
	GPURelated = models.ManyToManyField(Gpu)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name


class MotherBoard(models.Model):
	name = models.CharField(max_length=60)
	motherPatent = models.CharField(max_length=50)
	numberOfDIMMS = models.IntegerField(null = False,default=0)
	numberOfDisplaysSupported = models.IntegerField(null = False,default=0)
	maxNumberOfSataPorts = models.IntegerField(null = False,default=0)
	numberOfUSBPorts = models.IntegerField(null = False,default=0)
	USBRevision = models.CharField(max_length=100)
	busSpeed = models.FloatField(null = False,default=0.0)
	CPURelated = models.ManyToManyField(Cpu)
	GPURelated = models.ManyToManyField(Gpu)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.name
