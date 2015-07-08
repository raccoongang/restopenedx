# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('points_possible', models.IntegerField()),
                ('points_earned', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('usage_id', models.IntegerField()),
                ('instance_id', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
