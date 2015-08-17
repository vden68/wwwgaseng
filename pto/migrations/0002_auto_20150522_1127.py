# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spr_material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_material', models.CharField(max_length=100, verbose_name='\u0422\u0438\u043f \u0442\u0440\u0443\u0431\u044b')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0442\u0440\u0443\u0431\u044b',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0422\u0438\u043f\u043e\u0432 \u0442\u0440\u0443\u0431\u044b ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spr_pressure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_pressure', models.CharField(max_length=100, verbose_name='\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435 ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spr_tobject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_tobject', models.CharField(max_length=20, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044c\u0435\u043a\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spr_uzel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_uzel', models.CharField(max_length=100, verbose_name='\u0423\u0437\u0435\u043b')),
            ],
            options={
                'verbose_name': '\u0423\u0437\u0435\u043b',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0423\u0437\u043b\u044b ',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='spr_regulir_ustroystvo',
            options={'verbose_name': '\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e (\u0413\u0420\u041f\u0428)', 'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0440\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0438\u0445 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 (\u0413\u0420\u041f\u0428)'},
        ),
    ]
