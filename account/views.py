import json
from django.contrib.auth import get_user_model 
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.conf import settings

from .serializers import UserSerializer
from .models import User

# class Register(CreateAPIView):
#     permission_classes = (permissions.AllowAny, )
#     model = get_user_model()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
