# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0007_auto_20150525_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objekt',
            name='ge_databalans',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0431\u0430\u043b\u0430\u043d\u0441. \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_dateobsled',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_gosregisterdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_kadastrnomerdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u043a\u0430\u0434\u0430\u0441\u0442\u0440. \u0443\u0447\u0435\u0442', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_techuchetdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u0442\u0435\u0445. \u0443\u0447\u0435\u0442', blank=True),
            preserve_default=True,
        ),
    ]
