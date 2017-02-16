from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Admin panel
    url(r'^admin/', include(admin.site.urls)),

    # Login URLs
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}),

    # API
    url('^api/', include('oauth.api.urls')),

    # OAuth
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
