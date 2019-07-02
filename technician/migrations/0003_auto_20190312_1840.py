# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0002_auto_20190312_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techniciantoservice',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='rating', choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Average'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
