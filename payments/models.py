# payments/models.py
from django.db import models

from users.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.user.user_id} - {self.amount}"

    class Meta:
        db_table = "payment"
