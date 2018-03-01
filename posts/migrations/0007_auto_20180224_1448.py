# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-24 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='last_name',
        ),
        migrations.AddField(
            model_name='authors',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]