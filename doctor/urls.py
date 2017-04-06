from django.conf.urls import url

from .views import doctor_detail

urlpatterns = [
    url(r'^doctor/(?P<slug>[-\w]+)/$', doctor_detail, name='doctor_detail'),
]