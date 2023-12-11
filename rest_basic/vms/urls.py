from django.contrib import admin
from django.urls import path,include
from .views import VendorAPIView,VendorDetails,PurchaseOrderDetails,PurchaseOrderAPIView,VendorPerformanceDetails,AcknowledgementDetail #GenericAPIView

urlpatterns = [
    path('api/vendors/',VendorAPIView.as_view(),name="VendorAPIView"),
    path('api/vendors/<int:vendor_code>/',VendorDetails.as_view(),name="VendorDetails"),
    path('api/purchase_orders/',PurchaseOrderAPIView.as_view(),name="PurchaseOrderAPIView"),
    path('api/purchase_orders/<int:po_number>/',PurchaseOrderDetails.as_view(),name="PurchaseOrderDetails"),
    path('api/vendors/<int:vendor_code>/performance/',VendorPerformanceDetails.as_view(),name="VendorPerformanceDetails"),
    path('api/purchase_orders/<int:po_number>/acknowledge/',AcknowledgementDetail.as_view(),name="AcknowledgementDetail"),
    # path('test/',views.test,name="test"),
    # path('generic/vendor/<int:id>',GenericAPIView.as_view()),
]

