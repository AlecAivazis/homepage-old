# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='format',
            field=models.CharField(max_length=20, default='text'),
            preserve_default=False,
        ),
    ]
