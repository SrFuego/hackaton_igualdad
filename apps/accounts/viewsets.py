# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Account
from .serializers import AccountSerializer


# Create your viewsets here.
class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
