from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase  # Correct import statement
from .models import Vendor, PurchaseOrder, HistoricalPerformance,UniqueCode
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import VendorSerializer, PurchaseOrderSerializer,HistoricalPerformanceSerializer,AcknowledgementSerializer

class VendorTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = "test_user",password ="Anbc@123")

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        # UniqueCode.objects.create(name="Vendor",code=1000)
        # UniqueCode.objects.create(name="Po",code=100)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token.key)


    def test_one(self):
        """
        First Test Case For Vendor Post

        """

        url = reverse("VendorAPIView")
        data = {
            "id": 8,
            "name": "Pavan Sai",
            "contact_details": "9440138201",
            "address": "NehruNagar 7th Lane,Guntur,522008",
            "vendor_code": '1005',
            "on_time_delivery_rate": 0,
            "quality_rating_avg": 0,
            "average_response_time": 0,
            "fullfillment_rate": 0  # Correct the spelling here: fulfillment_rate
        }
        # self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(),1)
        self.assertEqual(Vendor.objects.get().name,"Pavan Sai")

    def test_two(self):
        """
        Test Case For Vendor put and delete

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1001', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        url = reverse("VendorDetails",args=[self.vendor.vendor_code])
        data = {
            "id": 8,
            "name": "Pavan Sai Narra",
            "contact_details": "9440138201",
            "address": "NehruNagar 7th Lane,Guntur,522008",
            "vendor_code": '1001',
            "on_time_delivery_rate": 0,
            "quality_rating_avg": 0,
            "average_response_time": 0,
            "fullfillment_rate": 0  # Correct the spelling here: fulfillment_rate
        }
        response = self.client.put(url, data, format="json")

        # url = reverse("VendorDetails")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(),1)
        self.assertEqual(Vendor.objects.get().name,"Pavan Sai Narra")

        url = reverse("VendorDetails",args=[1001])
        response = self.client.delete(url,format="json")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(),0)  


    def test_three(self):
        """

        test case for vendor get

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = "1001", contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        url = reverse("VendorAPIView")
        response = self.client.get(url,format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(),1)
        self.assertEqual(Vendor.objects.get().name,"Test Vendor")

    def test_four(self):

        """
        Test Case For get for a particular record

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1001', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        url = reverse("VendorDetails",args=[self.vendor.vendor_code])
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(),1)
        self.assertEqual(Vendor.objects.get().name,"Test Vendor")                


class PurchaseOrderTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = "test_user",password ="Anbc@123")

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        # UniqueCode.objects.create(name="Vendor",code=1000)
        # UniqueCode.objects.create(name="Po",code=100)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token.key)

    """
        first test for purchase order post

    """
    def test_five(self):
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1001', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        url = reverse("PurchaseOrderAPIView")
        data = {
            "id": 11,
            "po_number": "101",
            "order_date": "2023-12-09T09:40:32.880501Z",
            "delivery_date": "2023-12-09T18:00:00Z",
            "items": {
                "id": 2,
                "name": "Item 2",
                "description": "A second item for demonstration eeee.",
                "price": 29.99
            },
            "quantity": 2,
            "status": "Completed",
            "quality_rating": 4.5,
            "issue_date": "2023-12-09T09:40:32.880501Z",
            "acknowledgement_date": "2023-12-08T10:59:52Z",
            "vendor": self.vendor.id
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(),1)
        self.assertEqual(PurchaseOrder.objects.get().po_number,'100')

    def test_six(self):
        """
            test case for purchase order put request dot

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1001', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        purchase_order = PurchaseOrder.objects.create(po_number = '102', order_date='2023-01-01',
            quantity= 2,
            items = {
                    "data":"key"
                },
            status = "Completed",
            quality_rating = 4.5,
            issue_date= "2023-12-09T09:40:32.880501Z",
            acknowledgement_date = "2023-12-08T10:59:52Z",
            vendor =  self.vendor)
        data = {
            "id":1 ,
            "po_number": '102',
            "order_date": "2023-12-09T09:40:32.880501Z",
            "delivery_date": "2023-12-09T18:00:00Z",
            "items": {
                "id": 2,
                "name": "Item 2",
                "description": "A second item for demonstration eeee.",
                "price": 29.99
            },
            "quantity": 22,
            "status": "Completed",
            "quality_rating": 4.5,
            "issue_date": "2023-12-09T09:40:32.880501Z",
            "acknowledgement_date": "2023-12-08T10:59:52Z",
            "vendor": self.vendor.id
        }
        url = reverse('PurchaseOrderDetails',args=[102])
        response = self.client.put(url,data,format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(),1)
        self.assertEqual(PurchaseOrder.objects.get().quantity,22)

    def test_seven(self):
        """
            test case for purchase order delete request

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1003', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        purchase_order = PurchaseOrder.objects.create(po_number = '103', order_date='2023-01-01',
                quantity= 2,
                items = {
                        "data":"key"
                    },
                status = "Completed",
                quality_rating = 4.5,
                issue_date= "2023-12-09T09:40:32.880501Z",
                acknowledgement_date = "2023-12-08T10:59:52Z",
                vendor =  self.vendor)
        url = reverse('PurchaseOrderDetails',args=[103])
        response = self.client.delete(url,format="json")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(),0)

    def test_eight(self):
        """
            test case for purchase to get a particular order get request

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1004', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        self.purchase_order = PurchaseOrder.objects.create(po_number = '104', order_date='2023-01-01',
                quantity= 2,
                items = {
                        "data":"key"
                    },
                status = "Completed",
                quality_rating = 4.5,
                issue_date= "2023-12-09T09:40:32.880501Z",
                acknowledgement_date = "2023-12-08T10:59:52Z",
                vendor =  self.vendor)
        url = reverse('PurchaseOrderDetails',args=[104])
        response = self.client.get(url,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(),1)
        self.assertEqual(PurchaseOrder.objects.get().quantity,2)

    def test_nine(self):
        """
            test case for purchase to get a particular order(which is not present) get request

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1005', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        self.purchase_order = PurchaseOrder.objects.create(po_number = '105', order_date='2023-01-01',
                quantity= 2,
                items = {
                        "data":"key"
                    },
                status = "Completed",
                quality_rating = 4.5,
                issue_date= "2023-12-09T09:40:32.880501Z",
                acknowledgement_date = "2023-12-08T10:59:52Z",
                vendor =  self.vendor)
        url = reverse('PurchaseOrderDetails',args=[11])
        response = self.client.get(url,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(),1)

class HistoricalPerformanceTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = "test_user",password ="Anbc@123")
        # UniqueCode.objects.create(name="Vendor",code=1000)
        # UniqueCode.objects.create(name="Po",code=100)

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token.key)

    def test_ten(self):

        """
        Test Case For get for a particular record

        """
        self.vendor = Vendor.objects.create(name='Test Vendor', vendor_code = '1001', contact_details='123-456-7890', address='123 Test Street', on_time_delivery_rate = 0, quality_rating_avg = 0, average_response_time = 0, fullfillment_rate = 0)
        url = reverse("VendorPerformanceDetails",args=[self.vendor.vendor_code])
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HistoricalPerformance.objects.count(),1)
        self.assertEqual(HistoricalPerformance.objects.get().quality_rating_avg,self.vendor.quality_rating_avg)