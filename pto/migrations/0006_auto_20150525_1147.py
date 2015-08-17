# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0005_objekt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objekt',
            name='ge_gosregister',
            field=models.CharField(default=b'-', max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_gradsituazia',
            field=models.CharField(default=b'-', max_length=200, verbose_name='\u0413\u0440\u0430\u0434\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_ispolnitel',
            field=models.CharField(default=b'-', max_length=20, verbose_name='\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_izmertel',
            field=models.CharField(default=b'-', max_length=100, verbose_name='\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_kadastrnomer',
            field=models.CharField(default=b'-', max_length=10, verbose_name='\u041a\u0430\u0434\u0430\u0441\u0442\u0440\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_naznachenie',
            field=models.CharField(default=b'-', max_length=100, verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_nombuhucset',
            field=models.CharField(default=b'-', max_length=10, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0431\u0443\u0445. \u0443\u0447\u0435\u0442\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_opisanie',
            field=models.TextField(default=b'-', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_primech',
            field=models.TextField(default=b'-', verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_proekt',
            field=models.CharField(default=b'-', max_length=10, verbose_name='\u0428\u0438\u0444\u0440 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_techuchetnomer',
            field=models.CharField(default=b'-', max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u0445. \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430'),
            preserve_default=True,
        ),
    ]
