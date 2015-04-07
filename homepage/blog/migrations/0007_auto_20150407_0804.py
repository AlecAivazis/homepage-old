# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('blog', '0006_auto_20150404_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='format',
            field=models.CharField(max_length=20, default='markdown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag'),
            preserve_default=True,
        ),
    ]
