# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-25 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('F', 'Full'), ('P', 'Partial')], max_length=1)),
                ('start_point', models.CharField(max_length=50)),
                ('end_point', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trucks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_company_name', models.CharField(max_length=50)),
                ('truck_type', models.CharField(max_length=50)),
                ('start_point', models.CharField(max_length=50)),
                ('end_point', models.CharField(max_length=50)),
            ],
        ),
    ]