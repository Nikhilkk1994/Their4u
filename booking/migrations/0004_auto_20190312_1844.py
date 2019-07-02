# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190312_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='technician',
            field=models.ForeignKey(blank=True, to='technician.Technician', null=True),
        ),
    ]
