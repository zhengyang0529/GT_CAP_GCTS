# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-10 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20181010_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_dt',
            field=models.DateField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_dt',
            field=models.DateField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
