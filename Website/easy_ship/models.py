from django.db import models

class ServiceLevel(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Zone(models.Model):
	zip_code = models.CharField(max_length=3)
	service_level = models.ForeignKey(ServiceLevel)
	zone_number = models.CharField(max_length=3)
	
	def __unicode__(self):
		return "Zip code: " + self.zip_code + ", Service Level: " + self.service_level

class Rate(models.Model):
	weight = models.IntegerField()
	service_level = models.ForeignKey(ServiceLevel)
	zone_number = models.CharField(max_length=3)
	price = models.IntegerField()
	
	def __unicode__(self):
		return "Weight: " + self.weight + ", Service level: " + self.service_level + ", Zone: " + self.zone

	