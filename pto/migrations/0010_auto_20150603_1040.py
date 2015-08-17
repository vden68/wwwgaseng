# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0009_auto_20150526_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('pointobjekt_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pto.PointObjekt')),
                ('ge_tap', models.ForeignKey(verbose_name='\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0438(\u043a\u0440\u0430\u043d\u044b)', to='pto.Spr_tap')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0430(\u043a\u0440\u0430\u043d)',
                'verbose_name_plural': '\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0438(\u043a\u0440\u0430\u043d\u044b)',
            },
            bases=('pto.pointobjekt',),
        ),
        migrations.AlterModelOptions(
            name='regulir_ustroystvo',
            options={'verbose_name': '\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e', 'verbose_name_plural': '\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e'},
        ),
        migrations.AlterModelOptions(
            name='uzel',
            options={'verbose_name': '\u0423\u0437\u0435\u043b \u0433\u0430\u0437\u043e\u0432\u043e\u0439 \u0441\u0435\u0442\u0438', 'verbose_name_plural': '\u0423\u0437\u043b\u044b \u0433\u0430\u0437\u043e\u0432\u043e\u0439 \u0441\u0435\u0442\u0438'},
        ),
    ]
