# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0002_auto_20151027_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ['-url']},
        ),
    ]
