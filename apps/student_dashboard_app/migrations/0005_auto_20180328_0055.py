# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-28 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_dashboard_app', '0004_wish_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mine', to='student_dashboard_app.User'),
        ),
    ]
