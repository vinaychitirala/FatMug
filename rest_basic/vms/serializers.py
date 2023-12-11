from rest_framework import serializers
from .models import Vendor,PurchaseOrder,HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vendor
		# fields = ['name', 'contact_details', 'address','vendor_code']
		fields = '__all__'
		# exclude = ['vendor_code']

		# def create(self,validated_data):
		# 	gen_vendor_code = Vendor.gen_next_id()
		# 	validated_data['vendor_code'] = gen_vendor_code
		# 	return super().create(validated_data)

class PurchaseOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = PurchaseOrder
		# fields = ['name', 'contact_details', 'address','vendor_code']
		fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = HistoricalPerformance
		fields = '__all__'

class AcknowledgementSerializer(serializers.ModelSerializer):
	class Meta:
		model = PurchaseOrder
		fields = ['acknowledgement_date']
		