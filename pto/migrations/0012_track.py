# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0011_pipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_primech', models.TextField(default=b'-', verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435')),
                ('ge_endPoint', models.ForeignKey(related_name='endPoint', verbose_name='\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0442\u043e\u0447\u043a\u0430', to='pto.PointObjekt')),
                ('ge_objekt', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto.Objekt')),
                ('ge_pipe', models.ForeignKey(verbose_name='\u0422\u0440\u0443\u0431\u0430', to='pto.Pipe')),
                ('ge_startPoint', models.ForeignKey(related_name='startPoint', verbose_name='\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u043e\u0447\u043a\u0430', to='pto.PointObjekt')),
            ],
            options={
                'verbose_name': '\u0422\u0440\u0430\u0441\u0441\u0430 ',
                'verbose_name_plural': '\u0422\u0440\u0430\u0441\u0441\u0430',
            },
            bases=(models.Model,),
        ),
    ]
