from django.conf.urls import url, include
from django.contrib.auth import views
from . import view

urlpatterns = [
    url(r'^$', view.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]
