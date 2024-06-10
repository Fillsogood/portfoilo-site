from django.db import models

from common.models import CommonModel
from instructors.models import Instructor


class PilatesClass(CommonModel):
    class_name = models.CharField(max_length=200)
    description = models.TextField()
    class_time = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="classes")
