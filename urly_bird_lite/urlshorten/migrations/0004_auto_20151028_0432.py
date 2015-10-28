# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0003_auto_20151028_0429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='url',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
