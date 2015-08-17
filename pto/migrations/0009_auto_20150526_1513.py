# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0008_auto_20150525_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointObjekt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_naimen', models.CharField(max_length=30, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 ')),
                ('ge_nomer', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 (\u043b\u0438\u0442\u0435\u0440\u0430) ')),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0447\u043a\u0430 \u043e\u0431\u044c\u0435\u043a\u0442\u0430',
                'verbose_name_plural': '\u0422\u043e\u0447\u043a\u0438 \u043e\u0431\u044c\u0435\u043a\u0442\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Regulir_ustroystvo',
            fields=[
                ('pointobjekt_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pto.PointObjekt')),
                ('ge_regulir_ustroystvo', models.ForeignKey(verbose_name='\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e', to='pto.Spr_regulir_ustroystvo')),
            ],
            options={
            },
            bases=('pto.pointobjekt',),
        ),
        migrations.CreateModel(
            name='Uzel',
            fields=[
                ('pointobjekt_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pto.PointObjekt')),
                ('ge_uzel', models.ForeignKey(verbose_name='\u0423\u0437\u0435\u043b', to='pto.Spr_uzel')),
            ],
            options={
            },
            bases=('pto.pointobjekt',),
        ),
        migrations.AddField(
            model_name='pointobjekt',
            name='ge_objekt',
            field=models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto.Objekt'),
            preserve_default=True,
        ),
    ]
