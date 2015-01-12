
from django.conf.urls import patterns
from django.views.generic.base import TemplateView
from campaign.views import ChallengeView, ChallengeApplyView, CampaignCreateView, MyCampaignListView, CampaignUpdateView, CampaignHomeView
from django.conf.urls import url

urlpatterns = patterns('',

    (r'^explorer$',TemplateView.as_view(
        template_name="explorer/campaigns.html"
    )),
)