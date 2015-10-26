
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^params', views.params, name='params'),
]
