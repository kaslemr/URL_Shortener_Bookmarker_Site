# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0005_url_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='description',
        ),
    ]
