# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kdmail', '0002_auto_20151021_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edit_profile',
            name='id_field',
        ),
        migrations.RemoveField(
            model_name='edit_profile',
            name='pass_field',
        ),
        migrations.AddField(
            model_name='edit_profile',
            name='consultant_name',
            field=models.TextField(default=b'Enter Candidates Name'),
        ),
        migrations.AddField(
            model_name='edit_profile',
            name='job_location',
            field=models.TextField(default=b'Enter Job location for the Candidate'),
        ),
        migrations.AddField(
            model_name='edit_profile',
            name='technology',
            field=models.TextField(default=b'Enter domain for which to be marketted'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 12, 22)),
        ),
    ]
