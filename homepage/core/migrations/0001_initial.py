# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1020)),
                ('description', models.CharField(max_length=1020)),
                ('screenshot', models.FileField(upload_to='')),
                ('link', models.CharField(max_length=1020, blank=True)),
                ('type', models.CharField(max_length=10, choices=[('project', 'project'), ('research', 'research')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
