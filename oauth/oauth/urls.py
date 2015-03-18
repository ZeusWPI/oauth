from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}),

    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
