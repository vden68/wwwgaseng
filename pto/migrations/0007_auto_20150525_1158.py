# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0006_auto_20150525_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objekt',
            options={'verbose_name': '\u041e\u0431\u044c\u0435\u043a\u0442', 'verbose_name_plural': '\u041e\u0431\u044c\u0435\u043a\u0442\u044b \u0433\u0430\u0437\u043e\u0432\u043e\u0439 \u0441\u0435\u0442\u0438'},
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_databalans',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0431\u0430\u043b\u0430\u043d\u0441. \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_dateobsled',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_godpostr',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u0413\u043e\u0434 \u043f\u043e\u0441\u0442\u0440\u043e\u0439\u043a\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_godvvoda',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u0413\u043e\u0434 \u0432\u0432\u043e\u0434\u0430 \u0432 \u044d\u043a\u0441\u043f\u043b.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_gosregisterdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_kadastrnomerdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u043a\u0430\u0434\u0430\u0441\u0442\u0440. \u0443\u0447\u0435\u0442'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_kolizmertel',
            field=models.DecimalField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_plzastr',
            field=models.DecimalField(default=0, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0437\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_stbalans',
            field=models.DecimalField(default=0, verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objekt',
            name='ge_techuchetdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u0442\u0435\u0445. \u0443\u0447\u0435\u0442'),
            preserve_default=True,
        ),
    ]
