
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import CompanySerializer
from .models import Company


class CreateCompany(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    model = Company
    serializer_class = CompanySerializer

