# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Company')),
                ('owner', models.ForeignKey(to='customer.Customer')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companys',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Service name')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.ForeignKey(to='technician.Company')),
                ('user', models.OneToOneField(to='customer.Customer')),
            ],
            options={
                'verbose_name': 'technician',
                'verbose_name_plural': 'technicians',
            },
        ),
        migrations.CreateModel(
            name='TechnicianToService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fee', models.IntegerField(default=0, null=True, verbose_name='fee', blank=True)),
                ('rating', models.IntegerField(default=0, verbose_name='rating', choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Average'), ('4', 'Good'), ('5', 'Excellent')])),
                ('service_type', models.ForeignKey(to='technician.Service')),
                ('technician', models.ForeignKey(to='technician.Technician')),
            ],
            options={
                'verbose_name': 'service_to_technician',
                'verbose_name_plural': 'service_to_technicians',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='technicians',
            field=models.ManyToManyField(to='technician.Technician', through='technician.TechnicianToService'),
        ),
    ]
