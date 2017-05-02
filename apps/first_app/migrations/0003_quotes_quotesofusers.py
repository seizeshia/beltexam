# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20170501_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=255)),
                ('quotedby', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersid', to='first_app.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Quotesofusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotelink', to='first_app.Quotes')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlink', to='first_app.Users')),
            ],
        ),
    ]
