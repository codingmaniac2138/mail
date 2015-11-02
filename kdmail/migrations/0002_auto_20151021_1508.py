# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kdmail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='edit_profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id_field', models.TextField(default=b'Enter comma separated Gmail Ids')),
                ('pass_field', models.TextField(default=b'Enter comma separated passwords in sequence')),
            ],
        ),
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 10, 21))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.DeleteModel(
            name='mail_user',
        ),
    ]
