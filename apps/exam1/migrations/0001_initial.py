# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_auto_20161021_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=40)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('plan', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joined', models.ManyToManyField(related_name='joined', to='login.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planner', to='login.User')),
            ],
        ),
    ]
