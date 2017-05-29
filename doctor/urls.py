from django.conf.urls import url

from .views import doctor_detail, show_spec

urlpatterns = [
    url(r'^$', show_spec, name="show_spec"),
    url(r'^doctor/(?P<slug>[-\w]+)/$', doctor_detail, name='doctor_detail'),
]