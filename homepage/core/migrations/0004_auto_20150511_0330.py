# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project_screenshot'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectScreenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='screenshot',
        ),
        migrations.AddField(
            model_name='projectscreenshot',
            name='project',
            field=models.ForeignKey(related_name='screenshots', to='core.Project'),
        ),
    ]
