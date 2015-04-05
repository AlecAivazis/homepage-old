# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150401_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='screenshot',
            field=models.FileField(upload_to='', default=''),
            preserve_default=False,
        ),
    ]
