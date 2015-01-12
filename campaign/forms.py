
from django import forms
from campaign.models import Campaign, Challenge


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge