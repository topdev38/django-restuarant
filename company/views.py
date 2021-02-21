
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import CompanySerializer
from .models import Company


class CreateCompany(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    model = Company
    serializer_class = CompanySerializer
