from django.contrib import admin
from .models import Vendor,PurchaseOrder,HistoricalPerformance,UniqueCode
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
	list_display = ('id','name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fullfillment_rate')
admin.site.register(Vendor,VendorAdmin)

class PurchaseOrderAdmin(admin.ModelAdmin):
	list_display = ('id','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgement_date')
admin.site.register(PurchaseOrder,PurchaseOrderAdmin)

class HistoricalPerformanceAdmin(admin.ModelAdmin):
	list_display = ("id",'vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fullfillment_rate')
admin.site.register(HistoricalPerformance,HistoricalPerformanceAdmin)

class UniqueCodeAdmin(admin.ModelAdmin):
	list_display = ('id','name','code')
admin.site.register(UniqueCode,UniqueCodeAdmin)