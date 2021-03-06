# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heritage', '0002_auto_20161028_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='heritageobject',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='heritage.HeritageObject'),
        ),
    ]
