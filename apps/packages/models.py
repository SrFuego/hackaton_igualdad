# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel
from stdimage.models import StdImageField
from stdimage.utils import UploadToAutoSlugClassNameDir


# Local imports


# Create your models here.
class Package(TimeStampedModel):
    description = models.TextField()
    duration = models.CharField(max_length=50)
    image = StdImageField(
        upload_to=UploadToAutoSlugClassNameDir(populate_from="name"),
        variations={"thumbnail": (400, 250)})
    name = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField()

    @property
    def images(self):
        return self.activity_set.all()

    class Meta:
        verbose_name = "Paquete"

    def __str__(self):
        return self.name

    def image_admin_thumbnail(self):
        if self.image:
            return "<img src='{0}' alt='{1}'>".format(
                self.image.thumbnail.url, self.name)
        else:
            return "Sin imagen"

    image_admin_thumbnail.allow_tags = True


class Activity(models.Model):
    date = models.DateField()
    description = models.TextField()
    image = StdImageField(
        upload_to=UploadToAutoSlugClassNameDir(populate_from="name"),
        variations={"thumbnail": (400, 250)})
    name = models.CharField(max_length=50)
    package = models.ForeignKey("Package")
    time = models.TimeField()

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.name

    def image_admin_thumbnail(self):
        if self.image:
            return "<img src='{0}' alt='{1}'>".format(
                self.image.thumbnail.url, self.name)
        else:
            return "Sin imagen"

    image_admin_thumbnail.allow_tags = True
