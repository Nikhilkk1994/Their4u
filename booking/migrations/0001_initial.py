# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, verbose_name='status of booking', choices=[(0, 'Pending'), (1, 'Active'), (2, 'Complete'), (3, 'Cancelled')])),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('location', models.ForeignKey(to='customer.Location')),
            ],
            options={
                'verbose_name': 'booking',
                'verbose_name_plural': 'bookings',
            },
        ),
    ]
