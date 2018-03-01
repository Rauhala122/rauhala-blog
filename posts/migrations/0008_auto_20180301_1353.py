# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20180224_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.ManyToManyField(to='posts.Authors'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.CharField(blank=True, default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
