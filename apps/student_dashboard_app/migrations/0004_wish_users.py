# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-26 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dashboard_app', '0003_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='users',
            field=models.ManyToManyField(related_name='wishes_likes', to='student_dashboard_app.User'),
        ),
    ]