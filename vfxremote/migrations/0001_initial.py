# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ChoreList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='chore',
            name='chore_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vfxremote.ChoreList'),
        ),
    ]
