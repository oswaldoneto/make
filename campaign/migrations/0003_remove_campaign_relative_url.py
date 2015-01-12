# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_campaign_relative_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='relative_url',
        ),
    ]
