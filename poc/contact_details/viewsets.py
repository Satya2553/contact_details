from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import ContactSerailizer

class ContactViewSet(ModelViewSet):
    queryset = contact_det.objects.all()
    serializer_class = ContactSerailizer