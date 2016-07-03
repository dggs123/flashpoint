# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facemash', '0011_photo_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tag',
        ),
    ]
