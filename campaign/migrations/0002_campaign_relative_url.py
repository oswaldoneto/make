# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='relative_url',
            field=models.URLField(default='teste'),
            preserve_default=False,
        ),
    ]
