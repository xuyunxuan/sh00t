# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_templatemaster'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TemplateMaster',
        ),
    ]
