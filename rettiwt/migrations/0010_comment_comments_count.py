# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-14 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rettiwt', '0009_post_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
