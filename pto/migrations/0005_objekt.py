# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0004_auto_20150525_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objekt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_nomereestr', models.CharField(max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0440\u0435\u0435\u0441\u0442\u0440\u0430')),
                ('ge_nomeinvent', models.CharField(default=b'-', max_length=10, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('ge_naimenovanie', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('ge_naimenovaniekr', models.CharField(max_length=100, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('ge_naznachenie', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('ge_godpostr', models.PositiveSmallIntegerField(verbose_name='\u0413\u043e\u0434 \u043f\u043e\u0441\u0442\u0440\u043e\u0439\u043a\u0438')),
                ('ge_godvvoda', models.PositiveSmallIntegerField(verbose_name='\u0413\u043e\u0434 \u0432\u0432\u043e\u0434\u0430 \u0432 \u044d\u043a\u0441\u043f\u043b.')),
                ('ge_opisanie', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('ge_gradsituazia', models.CharField(max_length=200, verbose_name='\u0413\u0440\u0430\u0434\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u044f')),
                ('ge_izmertel', models.CharField(max_length=100, verbose_name='\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f')),
                ('ge_kolizmertel', models.DecimalField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=15, decimal_places=2)),
                ('ge_plzastr', models.DecimalField(verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0437\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438', max_digits=15, decimal_places=2)),
                ('ge_nombuhucset', models.CharField(max_length=10, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0431\u0443\u0445. \u0443\u0447\u0435\u0442\u0430')),
                ('ge_stbalans', models.DecimalField(verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', max_digits=15, decimal_places=2)),
                ('ge_databalans', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0431\u0430\u043b\u0430\u043d\u0441. \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438')),
                ('ge_proekt', models.CharField(max_length=10, verbose_name='\u0428\u0438\u0444\u0440 \u043f\u0440\u043e\u0435\u043a\u0442\u0430')),
                ('ge_kadastrnomer', models.CharField(max_length=10, verbose_name='\u041a\u0430\u0434\u0430\u0441\u0442\u0440\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('ge_kadastrnomerdata', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u043a\u0430\u0434\u0430\u0441\u0442\u0440. \u0443\u0447\u0435\u0442')),
                ('ge_techuchetnomer', models.CharField(max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u0445. \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430')),
                ('ge_techuchetdata', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u0442\u0435\u0445. \u0443\u0447\u0435\u0442')),
                ('ge_gosregister', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438')),
                ('ge_gosregisterdata', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438')),
                ('ge_primech', models.TextField(verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435')),
                ('ge_dateobsled', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('ge_ispolnitel', models.CharField(max_length=20, verbose_name='\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c')),
                ('ge_osnovanie', models.ForeignKey(verbose_name='\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435', to='pto.Osnovanie')),
                ('ge_tobject', models.ForeignKey(verbose_name='\u0422\u0438\u043f \u043e\u0431\u044c\u0435\u043a\u0442\u0430', to='pto.Spr_tobject')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044c\u0435\u043a\u0442',
                'verbose_name_plural': '\u041e\u0431\u044c\u0435\u043a\u0442\u044b \u0433\u0430\u0437\u043e\u0432\u043e\u0439 \u0441\u0435\u0442\u0438)',
            },
            bases=(models.Model,),
        ),
    ]
