# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cut_link', '0002_auto_20170203_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuturl',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]