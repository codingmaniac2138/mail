# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kdmail', '0004_edit_profile_requested_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='edit_profile',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to='kdmail.User'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 12, 23)),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='user',
            field=models.OneToOneField(to='kdmail.User'),
        ),
    ]
