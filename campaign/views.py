# Create your views here.
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from campaign.models import Campaign, Challenge
from campaign.forms import CampaignForm, ChallengeForm


class CampaignHomeView(ListView):
    model = Challenge
    template_name = 'campaign/campaign-home.html'


class ChallengeHomeView(DetailView):
    template_name = 'campaign/challenge.html'
    model = Challenge
    context_object_name="challenge"









#TODO: Refactor
class ChallengeView(TemplateView):
    template_name = 'campaign/challenge.html'


class ChallengeApplyView(RedirectView):
    url = "/campaign/1"
    def post(self, request, *args, **kwargs):
        c = Challenge.objects.get(id=4)
        u = User.objects.get(id=2)
        c.makers.add(u)
        c.state = 'RN'
        c.save()
        return super(ChallengeApplyView, self).post(request, *args, **kwargs)










class MyCampaignListView(ListView):
    model = Campaign
    template_name = "campaign/campaign-list.html"



class CampaignCreateView(CreateView):
    form_class = CampaignForm
    success_url = '/campaign/mine'
    template_name = 'campaign/campaign-form.html'


class CampaignUpdateView(UpdateView):
    model = Campaign
    form_class = CampaignForm
    success_url = '/campaign/mine'
    template_name = 'campaign/campaign-form.html'

