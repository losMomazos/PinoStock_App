from django.db import models

# Create your models here.
class Gpu(models.Model):
	modelGPU = models.CharField(max_length=60)
	patentGPU = models.CharField(max_length=50)
	baseCloack = models.FloatField(min_value = 0.001, max_value=1000.0)
	memoryCloack = models.FloatField(min_value = 0.001, max_value=1000.0)
	busSupport = models.CharField(max_length=30)
	memoryInterface = models.CharField(max_length=20)
	maximumDigitalResolution = models.CharField(max_length=30)
	recomendedSystemPower = models.FloatField(min_value = 0.001, max_value=1000.0)
	maximumTemperature = models.FloatField(min_value = 0.001, max_value=1000.0)
	CPURelated = models.ManyToManyField(Cpu)
	MotherBoardRelated = models.ManyToManyField(MotherBoard)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Cpu(models.Model):
	modelCPU = models.CharField(max_length=60)
	patentCPU = models.CharField(max_length=50)
	baseFrequency = models.FloatField(min_value = 0.001, max_value=1000.0)
	maxFrequency = models.FloatField(min_value = 0.00, max_value=1000.0)
	numberOfCores = models.IntegerField(min_value=1, max_value=50)
	numberOfThreads = models.IntegerField(min_value=1, max_value=50)
	socket = models.CharField(max_length=50)
	cache = models.IntegerField(min_value = 1, max_value = 1000)
	maxTemperature = models.FloatField(min_value = 0.0, max_value = 100.0)
	TDP = models.FloatField(min_value = 1.0, max_value=50.0)
	GPURelated = models.ManyToManyField(Gpu)
	MotherBoardRelated = models.ManyToManyField(MotherBoard)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name


class MotherBoard(models.Model):
	motherBoardName = models.CharField(max_length=60)
	motherPatent = models.CharField(max_length=50)
	numberOfDIMMS = models.IntegerField(min_value=1, max_value=50)
	numberOfDisplaysSupported = models.IntegerField(min_value=1, max_value=50)
	maxNumberOfSataPorts = models.IntegerField(min_value=1, max_value=50)
	numberOfUSBPorts = models.IntegerField(min_value=1, max_value=50)
	USBRevision = models.CharField(max_length=100)
	busSpeed = models.FloatField(min_value = 0.001, max_value=1000.0)
	CPURelated = models.ManyToManyField(Cpu)
	GPURelated = models.ManyToManyField(Gpu)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.name
