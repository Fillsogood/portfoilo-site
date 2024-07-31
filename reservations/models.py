# reservations/models.py
from django.db import models

from pilatesclass.models import PilatesClass
from users.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    class_info = models.ForeignKey(PilatesClass, on_delete=models.CASCADE, related_name="reservations")
    reserved_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="reserved")

    def __str__(self) -> str:
        return f"{self.user.user_id} - {self.class_info.name}"

    class Meta:
        db_table = "reservation"
