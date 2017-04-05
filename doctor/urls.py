from django.conf.urls import url, include

from .views import doctor_detail

urlpatterns = [
    url(r'^doctor/(?P<slug>[-\w]+)/$', doctor_detail, name='doctor_detail'),
]