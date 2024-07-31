from typing import Any, Optional, TypeVar

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# 사용자 모델 타입 변수 정의
UserType = TypeVar("UserType", bound="User")


class UserManager(BaseUserManager[UserType]):
    def create_user(self, user_id: str, password: str, **extra_fields: Any) -> UserType:
        if not user_id:
            raise ValueError("User ID must be provided")

        user: UserType = self.model(user_id=user_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id: str, password: str, **extra_fields: Any) -> UserType:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "user"
