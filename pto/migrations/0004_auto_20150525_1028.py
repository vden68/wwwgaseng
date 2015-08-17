# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0003_spr_tap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Osnovanie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_osnovanie', models.CharField(max_length=100, verbose_name='\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u0438\u0435\u043c\u0430 \u043d\u0430 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='spr_regulir_ustroystvo',
            options={'verbose_name': '\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e (\u0413\u0420\u041f\u0428)', 'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0438\u0445 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 (\u0413\u0420\u041f\u0428)'},
        ),
    ]
