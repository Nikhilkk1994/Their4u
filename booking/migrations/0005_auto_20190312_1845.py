# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190312_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='customer',
        ),
    ]
