from django.conf.urls import url

from .views import CreateCompany

urlpatterns = [
    url(r'^new/$', CreateCompany.as_view(), name='create_company'),
]