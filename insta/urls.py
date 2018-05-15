from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views
from . import view

urlpatterns = [
    url(r'^$', view.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', view.profile, name = 'profile'),
    url(r'^(?P<user_id>[0-9]+)/edits/$', view.profile_edit, name='profile_edit'),
    url(r'^Post/New/$', view.post, name='post'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
