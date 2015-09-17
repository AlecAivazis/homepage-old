# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150511_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(max_length=1020, blank=True),
            preserve_default=True,
        ),
    ]
