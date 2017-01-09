# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kdmail', '0005_auto_20161223_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consultant_name', models.TextField(default=b'Enter Candidates Name')),
                ('technology', models.TextField(default=b'Enter domain for which to be marketted')),
                ('job_location', models.TextField(default=b'Enter Job location for the Candidate')),
                ('requested_email', models.EmailField(default=b'email', max_length=254)),
                ('requirements_count', models.IntegerField()),
                ('date_added', models.DateField(default=datetime.date(2017, 1, 9))),
            ],
        ),
        migrations.AlterField(
            model_name='edit_profile',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 1, 9)),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='user_stats',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
