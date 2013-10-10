from django.db import models
from django.contrib import admin


class Campaign(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.name


class Opportunity(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign)
    skill = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title


admin.site.register(Campaign)
admin.site.register(Opportunity)