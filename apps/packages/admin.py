# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Activity, Package


# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "image_admin_thumbnail",)
    list_filter = ("package",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "image_admin_thumbnail",)
