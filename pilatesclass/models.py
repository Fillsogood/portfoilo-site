# classes/models.py
from django.db import models

from users.models import User


class PilatesClass(models.Model):
    name = models.CharField(max_length=100)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pilatesclass")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "pilatesclass"
