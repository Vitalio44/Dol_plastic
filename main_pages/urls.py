from django.conf.urls import url, include

from main_pages.views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]