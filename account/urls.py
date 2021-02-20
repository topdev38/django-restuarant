from django.conf.urls import url
from django.urls import path

from .views import Register, Profile

urlpatterns = [
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^profile/$', Profile.as_view(), name='profile')
]