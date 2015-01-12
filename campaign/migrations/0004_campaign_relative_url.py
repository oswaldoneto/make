# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_remove_campaign_relative_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='relative_url',
            field=models.CharField(default='teste', max_length=160),
            preserve_default=False,
        ),
    ]
