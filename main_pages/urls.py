from django.conf.urls import url

from main_pages.views import index, show_page

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<page_slug>[-\w]+)/$', show_page, name='show_page'),
]

