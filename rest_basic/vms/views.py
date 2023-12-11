from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Vendor,PurchaseOrder,HistoricalPerformance,UniqueCode
from .serializers import VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer,AcknowledgementSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.signals import post_save
# Create your views here.

# class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
# 	serializer_class = VendorSerializer
# 	queryset = Vendor.objects.all()
# 	lookup_field = 'id'
# 	authentication_classes = [TokenAuthentication]
# 	permission_classes = [IsAuthenticated]

# 	def get(self,request,id=None):
# 		if id:
# 			return self.retrieve(request)
# 		else:
# 			return self.list(request)

# 	def post(self,request):
# 		return self.update(request,id)

# 	def put(self,request,id=None):
# 		return self.update(request,id)

# 	def delete(self,request,id):
# 		return self.destroy(request,id)

# @api_view(['GET','POST'])
class VendorAPIView(APIView):

	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self,request):
		vendor = Vendor.objects.all()
		serializer = VendorSerializer(vendor,many=True)
		return Response(serializer.data,status=status.HTTP_201_CREATED)

	def post(self,request):
		# print("aaaaaaaaaaaaaaaaaaa")
		serializer = VendorSerializer(data=request.data)

		if serializer.is_valid():
			# print(serializer.data)
			# print("trueeee")
			vc_ref = UniqueCode.objects.get(name="Vendor")
			serializer.validated_data['vendor_code']=str(vc_ref.code)
			vc_ref.code += 1
			vc_ref.save()
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)			



# @api_view(['GET','PUT','DELETE'])
class VendorDetails(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def bring_object(self,vendor_code):
		try:
			return Vendor.objects.get(vendor_code=str(vendor_code))
		except Vendor.DoesNotExist :
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)
	def get(self,request,vendor_code):
		vendor = self.bring_object(vendor_code)
		try:
			serializer = VendorSerializer(vendor)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		except:
			data = "No Recors Found"
			return Response(data,status=status.HTTP_400_BAD_REQUEST)


	def put(self,request,vendor_code):
		vendor = self.bring_object(vendor_code)
		serializer = VendorSerializer(vendor,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,vendor_code):
		vendor = self.bring_object(vendor_code)
		vendor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

#po
# @api_view(['GET','POST'])
class PurchaseOrderAPIView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self,request):
		po = PurchaseOrder.objects.all()
		serializer = PurchaseOrderSerializer(po,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = PurchaseOrderSerializer(data=request.data)
		if serializer.is_valid():
			po_ref = UniqueCode.objects.get(name="Po")
			serializer.validated_data['po_number']=str(po_ref.code)
			po_ref.code += 1
			po_ref.save()
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)			



# @api_view(['GET','PUT','DELETE'])
class PurchaseOrderDetails(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get_object(self,po_number):
		try:
			return PurchaseOrder.objects.get(po_number=str(po_number))
		except:
			data = "No Record Found"
			return Response(data,status=status.HTTP_400_BAD_REQUEST)
	def get(self,request,po_number):
		po = self.get_object(po_number)
		try:
			serializer = PurchaseOrderSerializer(po)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		except:
			data = "No Recors Found"
			return Response(data,status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,po_number):
		po = self.get_object(po_number)
		serializer = PurchaseOrderSerializer(po,data=request.data)
		if serializer.is_valid():
			serializer.save() #data from post method is updated after validating
			return Response(serializer.data,status=status.HTTP_201_CREATED)
			# return HttpResponse(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,po_number):
		po = self.get_object(po_number)
		po.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class VendorPerformanceDetails(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get_object(self,vendor_code):
		try:
			return Vendor.objects.get(vendor_code=str(vendor_code))
		except Vendor.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)


	def get(self,request,vendor_code):
		vendor = self.get_object(vendor_code)
		try:
			hp = HistoricalPerformance.objects.get(vendor=vendor)
			serializer = HistoricalPerformanceSerializer(hp)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		except:
			data = "No Recors Found"
			return Response(data,status=status.HTTP_400_BAD_REQUEST)

class AcknowledgementDetail(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get_object(self,po_number):
		try:
			return PurchaseOrder.objects.get(po_number=str(po_number))
		except:
			data = "No Record Found"
			return Response(data,status=status.HTTP_400_BAD_REQUEST)
	
	def get(self,request,po_number):
		po = self.get_object(po_number)
		try:
			serializer = AcknowledgementSerializer(po)
			return Response(serializer.data)
		except:
			data = "No Recors Found"
			return Response(data,status=status.HTTP_400_BAD_REQUEST)



	def put(self,request,po_number):
		po = self.get_object(po_number)
		serializer = AcknowledgementSerializer(po,data=request.data)
		if serializer.is_valid():
			serializer.save() 
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)