# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_sys', '0011_auto_20170319_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_item_available',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='exemplares disponíveis'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_item_total',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='total de exemplares'),
        ),
    ]