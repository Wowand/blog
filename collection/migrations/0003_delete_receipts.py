# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_receipts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Receipts',
        ),
    ]
