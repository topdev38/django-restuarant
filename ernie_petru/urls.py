
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from account.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('company/', include('company.urls')),
    path('order/', include('order.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
