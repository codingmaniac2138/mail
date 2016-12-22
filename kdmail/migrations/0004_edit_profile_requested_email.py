# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kdmail', '0003_auto_20161222_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit_profile',
            name='requested_email',
            field=models.EmailField(default=b'Enter email you want to recv reqs', max_length=254),
        ),
    ]
