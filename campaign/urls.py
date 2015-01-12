
from django.conf.urls import patterns
from campaign.views import ChallengeView, ChallengeApplyView, CampaignCreateView, MyCampaignListView, CampaignUpdateView, CampaignHomeView, ChallengeHomeView
from django.conf.urls import url

urlpatterns = patterns('',

    (r'^campaign/mine$',MyCampaignListView.as_view()),
    (r'^campaign/create$', CampaignCreateView.as_view()),
    (r'^campaign/update/(?P<pk>[\w-]+)$', CampaignUpdateView.as_view()),


    #TODO: Refactor
    (r'^campaign/(?P<pk>\d+)/$', CampaignHomeView.as_view()),
    (r'^campaign/1/challenge/(?P<pk>\d+)/$', ChallengeHomeView.as_view()),
    (r'^campaign/(?P<campaign>\d+)/challenge/(?P<challenge>\d+)/apply$', ChallengeApplyView.as_view()),
)