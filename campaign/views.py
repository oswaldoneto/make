# Create your views here.
from django.views.generic.list import ListView
from campaign.models import Campaign, Challenge


class CampaignView(ListView):
    model = Challenge
    template_name = 'campaign/campaign.html'

