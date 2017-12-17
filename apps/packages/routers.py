# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PackageViewSet


# Create your routers here.
packages = (
    (r"package", PackageViewSet),
)
