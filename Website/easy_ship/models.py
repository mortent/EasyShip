from django.db import models

class ServiceLevels(models.Model):
	name = models.CharField(max_length=100)

class ZoneChart(models.Model):
	zip_code = models.CharField(max_length=3)
	service_level = models.ForeignKey(ServiceLevels)
	zone = models.CharField(max_length=3)

class RateChart(models.Model):
	weight = models.IntegerField()
	service_level = models.ForeignKey(ServiceLevels)
	zone = models.CharField(max_length=3)
	price = models.IntegerField()

	