# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_change_pointer_file_filegrpuse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfailmessage',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, db_column=b'pk'),
        ),
        migrations.AlterField(
            model_name='jobfailmessage',
            name='message',
            field=models.CharField(max_length=1000, null=True, db_column=b'Message', blank=True),
        ),
        migrations.AlterField(
            model_name='jobfailmessage',
            name='microservicechainlink',
            field=models.ForeignKey(db_column=b'microServiceChainLinksPK', to='main.MicroServiceChainLink', null=True),
        ),
    ]
