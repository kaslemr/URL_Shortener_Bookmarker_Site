# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0004_auto_20151028_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='description',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
    ]
