from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	isCA=models.BooleanField(default=False)
	phone_number=models.BigIntegerField(null=True)
	birthdate=models.DateField(null=True)
