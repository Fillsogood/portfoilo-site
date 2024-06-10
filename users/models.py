from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


def profile_image_path(instance: "User", filename: str) -> str:
    # 파일이 업로드될 경로를 지정하는 함수
    return f"users/profile_images/{filename}"


class UserManager(BaseUserManager["User"]):
    def create_user(self, user_id: str, password: str, **extra_fields: Any) -> "User":
        if not user_id:
            raise ValueError("Users must have an email address")

        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id: str, password: str, **extra_fields: Any) -> "User":
        user = self.create_user(user_id, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to=profile_image_path, null=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_id"
