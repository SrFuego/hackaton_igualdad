# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("__str__", "location", "dni", "cell_phone",)
    list_filter = ("location",)
