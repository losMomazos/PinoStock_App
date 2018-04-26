from django.db import models

# Create your models here.
class Gpu(models.Model):
	modelGPU = models.CharField(max_length=60)
	patentGPU = models.CharField(max_length=50)
	baseCloack = models.FloatField(null = False)
	memoryCloack = models.FloatField(null = False)
	busSupport = models.CharField(max_length=30)
	memoryInterface = models.CharField(max_length=20)
	maximumDigitalResolution = models.CharField(max_length=30)
	recomendedSystemPower = models.FloatField(null = False)
	maximumTemperature = models.FloatField(null = False)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Cpu(models.Model):
	modelCPU = models.CharField(max_length=60)
	patentCPU = models.CharField(max_length=50)
	baseFrequency = models.FloatField(null = False)
	maxFrequency = models.FloatField(null = False)
	numberOfCores = models.IntegerField(null = False)
	numberOfThreads = models.IntegerField(null = False)
	socket = models.CharField(max_length=50)
	cache = models.IntegerField(min_value = 1, max_value = 1000)
	maxTemperature = models.FloatField(null = False)
	TDP = models.FloatField(null = False)
	GPURelated = models.ManyToManyField(Gpu)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name


class MotherBoard(models.Model):
	motherBoardName = models.CharField(max_length=60)
	motherPatent = models.CharField(max_length=50)
	numberOfDIMMS = models.IntegerField(null = False)
	numberOfDisplaysSupported = models.IntegerField(null = False)
	maxNumberOfSataPorts = models.IntegerField(null = False)
	numberOfUSBPorts = models.IntegerField(null = False)
	USBRevision = models.CharField(max_length=100)
	busSpeed = models.FloatField(null = False)
	CPURelated = models.ManyToManyField(Cpu)
	GPURelated = models.ManyToManyField(Gpu)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.name
