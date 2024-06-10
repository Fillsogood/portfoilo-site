from django.db import models

from common.models import CommonModel
from reservations.models import Reservation


class Payment(CommonModel):
    STATUS_CHOICES = [
        ("Paid", "Paid"),
        ("Cancelled", "Cancelled"),
    ]

    PAYMENT_METHOD_CHOICES = [
        ("CreditCard", "Credit Card"),
        ("BankTransfer", "Bank Transfer"),
        ("PayPal", "PayPal"),
    ]

    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Paid")
