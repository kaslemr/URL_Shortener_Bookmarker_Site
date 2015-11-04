# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0008_clickcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
