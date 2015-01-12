from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.db.models.base import get_absolute_url


class Campaign(models.Model):
    name = models.CharField(max_length=160)
    message = models.CharField(max_length=160)
    start_date = models.DateField()
    end_date = models.DateField()
    relative_url = models.CharField(max_length=160)

    def __unicode__(self):
        return self.name


class Challenge(models.Model):
    AVAILABILITY_CHOICES = (
        ('FL', 'Freelance'),
        ('FT', 'Full-time'),
    )
    STATE_CHOICES = (
        ('NW', 'New'),
        ('RN', 'Running'),
        ('FD', 'Finished'),
        ('CD', 'Canceled'),
    )
    title = models.CharField(max_length=160)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign)
    image = models.CharField(max_length=250, blank=True)
    job_profile = models.CharField(max_length=50, blank=True)
    skill_required = models.CharField(max_length=50, blank=True)
    due_date = models.DateField(null=True,blank=True)
    job_estimate = models.CharField(max_length=50, blank=True)
    reward = models.CharField(max_length=50, blank=True)
    availability = models.CharField(max_length=2, choices=AVAILABILITY_CHOICES)
    makers = models.ManyToManyField(User)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)

    def __unicode__(self):
        return self.title


admin.site.register(Campaign)
admin.site.register(Challenge)