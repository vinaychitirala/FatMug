from django.db.models.signals import post_save,pre_save,post_migrate
from django.dispatch import receiver
from django.db.models import F, Avg, Count
from django.utils import timezone
from .models import Vendor, PurchaseOrder, HistoricalPerformance,UniqueCode

@receiver(post_migrate)
def create_initial_records(sender, **kwargs):
    if sender.name == 'vms':  # Replace 'yourapp' with the name of your app
        UniqueCode.objects.create(name='Vendor', code=1000)
        UniqueCode.objects.create(name='Po', code=100)
# @receiver(pre_save, sender=Vendor) #instance
# def genn_vendor_code(sender,instance,**kwargs):
#     if Vendor.flag:
#         vendor_code_count = Vendor.objects.get(vendor_code=instance.vendor_code).count()
#         if vendor_code_count == 0:
#             print(vendor_code_list,'hell')
#             last_vendor = Vendor.objects.order_by('-id').first()
#             if last_vendor:
#                 instance.vendor_code=str(int(last_vendor.vendor_code)+1)
#             else:
#                 instance.vendor_code=str(sender.vendor_unique_code)
#         else:
#             pass
#     else:
#         Vendor.flag=True
# @receiver(pre_save,sender=PurchaseOrder)
# def update_po_number(sender,instance,**kwargs):
#     Vendor.flag = False
#     last_po = PurchaseOrder.objects.order_by('-id').first()
#     if last_po:
#         instance.po_number=str(int(last_po.po_number)+1)
#     else:
#         instance.po_number=str(sender.po_number_unique)


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, created, **kwargs):
    # if not created:
    if True:
        # Update on-time delivery rate
        if instance.status == 'Completed':
            completed_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='Completed')
            total_completed_pos = PurchaseOrder.objects.filter(vendor=instance.vendor).count()
            on_time_deliveries = completed_pos.count()
            instance.vendor.on_time_delivery_rate = on_time_deliveries / total_completed_pos

        # # Update quality rating average
        if instance.quality_rating is not None:
            completed_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='Completed', quality_rating__isnull=False).values_list('quality_rating')
            instance.vendor.quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg']
        
        # # Update average response time
        if instance.acknowledgement_date is not None: #acknowledgement_date
            acknowledged_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgement_date__isnull=False)
            response_times = [abs(po.acknowledgement_date - po.issue_date).total_seconds() for po in acknowledged_pos]
            repo_time= sum(response_times) / len(response_times) if len(response_times) > 0 else 0
            instance.vendor.average_response_time = repo_time/60
        
        # Update fulfillment rate
        all_pos = PurchaseOrder.objects.filter(vendor=instance.vendor).count()
        successful_fulfillments = PurchaseOrder.objects.filter(vendor = instance.vendor,status="Completed").count()
        instance.vendor.fullfillment_rate = (successful_fulfillments / all_pos) 

        # Save the vendor instance
        instance.vendor.save()

@receiver(post_save, sender=Vendor)
def update_historical_performance(sender, instance,created, **kwargs):
    if  created:
        HistoricalPerformance.objects.create(
            vendor=instance,
            on_time_delivery_rate=instance.on_time_delivery_rate,
            quality_rating_avg = instance.quality_rating_avg,
            average_response_time = instance.average_response_time,
            fullfillment_rate = instance.fullfillment_rate
        )
    else:
        hp = HistoricalPerformance.objects.get(vendor=instance)
        hp.on_time_delivery_rate = instance.on_time_delivery_rate
        hp.quality_rating_avg=instance.quality_rating_avg
        hp.average_response_time=instance.average_response_time
        hp.fullfillment_rate=instance.fullfillment_rate
        hp.save()
