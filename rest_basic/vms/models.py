from django.db import models

class UniqueCode(models.Model):

	name = models.CharField(max_length=255)
	code = models.IntegerField()

# Create your models here.
class Vendor(models.Model):
	vendor_unique_code = 1000
	flag = True
	name = models.CharField(max_length=255)
	contact_details = models.TextField()
	address = models.TextField()
	vendor_code = models.CharField(null=True,max_length=255)
	# vendor_code = UniqueCode.objects.get(pk=3).code
	on_time_delivery_rate = models.FloatField()
	quality_rating_avg = models.FloatField()
	average_response_time = models.FloatField()
	fullfillment_rate = models.FloatField()

	def __str__(self):
		return self.name

class PurchaseOrder(models.Model):
	po_number_unique = 100
	po_number = models.CharField(null=True,max_length=255)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	order_date = models.DateTimeField(auto_now_add=True)
	delivery_date = models.DateTimeField(null=True)
	items = models.JSONField()
	quantity = models.IntegerField()
	status = models.CharField(max_length=255)
	quality_rating = models.FloatField()
	issue_date = models.DateTimeField(auto_now_add=True)
	acknowledgement_date = models.DateTimeField(auto_now_add=False)

	def __str__(self):
		return self.po_number

class HistoricalPerformance(models.Model):

	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	on_time_delivery_rate = models.FloatField()
	quality_rating_avg = models.FloatField()
	average_response_time = models.FloatField()
	fullfillment_rate = models.FloatField()

	def __str__(self):
		return self.vendor.name




