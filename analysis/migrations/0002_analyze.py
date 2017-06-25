# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='analyze',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workbk', models.CharField(max_length=20, blank=True)),
                ('no_sub', models.CharField(max_length=20, blank=True)),
                ('new_file', models.CharField(max_length=20, blank=True)),
                ('credit', models.CharField(max_length=20, blank=True)),
            ],
        ),
    ]
