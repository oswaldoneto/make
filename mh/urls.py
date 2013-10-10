from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.base import TemplateView
from mh import settings
from campaign.views import CampaignView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', TemplateView .as_view(
        template_name="home.html"
    )),

    (r'^campaign/(?P<campaign>\d+)$',CampaignView.as_view()),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


