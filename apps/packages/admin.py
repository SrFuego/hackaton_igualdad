# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Activity, Package


# Register your models here.
admin.site.register(Activity)
admin.site.register(Package)
