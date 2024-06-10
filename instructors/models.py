from django.db import models

from common.models import CommonModel


class Instructor(CommonModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
