# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 05:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160906_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 8, 5, 20, 50, 670572, tzinfo=utc)),
        ),
    ]
