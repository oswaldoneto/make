# Create your views here.
from django.views.generic.list import ListView
from campaign.models import Campaign, Opportunity


class CampaignView(ListView):
    model = Opportunity
    template_name = 'campaign/campaign.html'

