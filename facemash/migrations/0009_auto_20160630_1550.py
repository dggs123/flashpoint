# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facemash', '0008_auto_20160630_1526'),
    ]

    operations = [
        migrations.DeleteModel(
            name='rank_db',
        ),
        migrations.DeleteModel(
            name='total_likes',
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name_plural': 'Facemash'},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='Discription',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='nlikes',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='width_field',
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(null=True, upload_to='facemash_photos'),
        ),
        migrations.AddField(
            model_name='photo',
            name='ratings',
            field=models.FloatField(default=1500),
        ),
        migrations.AddField(
            model_name='photo',
            name='rd',
            field=models.FloatField(default=350),
        ),
        migrations.AddField(
            model_name='photo',
            name='sigma',
            field=models.FloatField(default=0.06),
        ),
    ]
