from django.db import models

from members.models import Member
from pilatesclass.models import PilatesClass


# 회원 수업 예약
class Reservation(models.Model):
    STATUS_CHOICES = [
        ("Reserved", "Reserved"),
        ("Cancelled", "Cancelled"),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="reservations")
    class_name = models.ForeignKey(PilatesClass, on_delete=models.CASCADE, related_name="reservations")
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Reserved")
