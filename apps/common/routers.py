# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter

# Local imports
# from ..app_django.routers import router_list as app_django_router
from ..accounts.routers import accounts
from ..packages.routers import packages

# Create your routers here.
routers_tuples = (accounts, packages,)
routers_lists = sum(
    [list(router_tuple) for router_tuple in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    router.register(router_list[0], router_list[1])
