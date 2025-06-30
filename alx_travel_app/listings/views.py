from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.conf import settings
#import requests
import os
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
CHAPA_SECRET_KEY = os.getenv("CHAPA_SECRET_KEY")

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Save booking with current logged-in user
        serializer.save(user=self.request.user)
        booking = serializer.instance

        amount = booking.listing.price  # We use listing price
        email = booking.user.email
        first_name = booking.user.first_name or "Guest"
        last_name = booking.user.last_name or "User"

        payload = {
            "amount": str(amount),
            "currency": "ETB",
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "tx_ref": f"booking_{booking.id}",
            "callback_url": "http://127.0.0.1:8000/verify/",
            "return_url": "http://127.0.0.1:8000/success/",
            "customization[title]": "Booking Payment",
            "customization[description]": f"Payment for booking {booking.id}"
        }

        headers = {
            "Authorization": f"Bearer {CHAPA_SECRET_KEY}"
        }

        response = requests.post("https://api.chapa.co/v1/transaction/initialize", json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            payment = Payment.objects.create(
                booking=booking,
                amount=amount,
                status="Pending",
                transaction_id=data['data']['tx_ref']
            )
            return Response({
                "checkout_url": data['data']['checkout_url'],
                "payment_id": payment.id,
                "message": "Payment initiated successfully."
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to initiate payment"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='verify-payment')
    def verify_payment(self, request, pk=None):
        booking = self.get_object()
        payment = get_object_or_404(Payment, booking=booking)

        headers = {
            "Authorization": f"Bearer {CHAPA_SECRET_KEY}"
        }

        verify_url = f"https://api.chapa.co/v1/transaction/verify/{payment.transaction_id}"

        response = requests.get(verify_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success' and data['data']['status'] == 'success':
                payment.status = "Completed"
                payment.save()
                return Response({"message": "Payment verified and completed."}, status=status.HTTP_200_OK)
            else:
                payment.status = "Failed"
                payment.save()
                return Response({"message": "Payment verification failed or incomplete."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Failed to verify payment."}, status=status.HTTP_400_BAD_REQUEST)
        
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer        
