# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kdmail', '0006_auto_20170109_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 1, 31)),
        ),
        migrations.AlterField(
            model_name='user_stats',
            name='date_added',
            field=models.DateField(default=datetime.date(2017, 1, 31)),
        ),
    ]
