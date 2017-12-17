# Python imports


# Django imports
from django.conf import settings
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Account(TimeStampedModel):
    cell_phone = models.CharField(max_length=9, verbose_name="celular")
    dni = models.CharField(max_length=8, unique=True)
    ubigeo = models.CharField(max_length=50)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="account",
        verbose_name="Usuario")

    class Meta:
        verbose_name = "Cuenta"

    def __str__(self):
        return self.user.get_full_name()
