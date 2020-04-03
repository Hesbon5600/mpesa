from django.urls import path
from .views import PaymentAPIView, ConfirmPaymentAPIView


urlpatterns = [
    path('donate', PaymentAPIView.as_view(), name='add-debit-card'),
    path('confirm/<str:transaction_id>/', ConfirmPaymentAPIView.as_view(), name='confirm'),
]
