# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0002_auto_20150522_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spr_tap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_tap', models.CharField(max_length=100, verbose_name='\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0438(\u043a\u0440\u0430\u043d\u044b)')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0430 (\u043a\u0440\u0430\u043d)',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0417\u0430\u0434\u0432\u0438\u0436\u0435\u043a (\u043a\u0440\u0430\u043d\u043e\u0432)',
            },
            bases=(models.Model,),
        ),
    ]
