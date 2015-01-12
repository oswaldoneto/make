# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=160)),
                ('message', models.CharField(max_length=160)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True)),
                ('job_profile', models.CharField(max_length=50, blank=True)),
                ('skill_required', models.CharField(max_length=50, blank=True)),
                ('due_date', models.DateField(null=True, blank=True)),
                ('job_estimate', models.CharField(max_length=50, blank=True)),
                ('reward', models.CharField(max_length=50, blank=True)),
                ('availability', models.CharField(max_length=2, choices=[(b'FL', b'Freelance'), (b'FT', b'Full-time')])),
                ('state', models.CharField(max_length=2, choices=[(b'NW', b'New'), (b'RN', b'Running'), (b'FD', b'Finished'), (b'CD', b'Canceled')])),
                ('campaign', models.ForeignKey(to='campaign.Campaign')),
                ('makers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
