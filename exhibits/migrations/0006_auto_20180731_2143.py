# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-31 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0005_exhibititem_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit',
            name='copyright_holder',
            field=models.TextField(default='Regents of the University of California'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibit',
            name='copyright_year',
            field=models.IntegerField(default='2011'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibit',
            name='curator',
            field=models.TextField(default='University of California'),
            preserve_default=False,
        ),
    ]
