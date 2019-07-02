# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
        ('technician', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='service_type',
            field=models.ForeignKey(to='technician.Service'),
        ),
        migrations.AddField(
            model_name='booking',
            name='technician',
            field=models.ForeignKey(to='technician.Technician'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(to='customer.Customer'),
        ),
    ]
