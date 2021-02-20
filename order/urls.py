from django.conf.urls import url

from .views import OrderList

urlpatterns = [
    url(r'^order/$', OrderList.as_view(), name='order'),
]