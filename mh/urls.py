from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from mh import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/campaign/1'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('explorer.urls')),
    url(r'', include('campaign.urls')),
    #redirect traffic that doesnt match any of my other URLs back to /make
    #url(r'^.*$', RedirectView.as_view(url='/make', permanent=False), name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


