from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers

router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^current_user/', 'oauth.api.get_current_user.current_user'),
)
