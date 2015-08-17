# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pto.models


class Migration(migrations.Migration):

    dependencies = [
        ('pto', '0012_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjektFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_objektFile', models.FileField(upload_to=pto.models.objekt_upload_path)),
                ('ge_uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('ge_objekt', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto.Objekt')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('ge_objekt', 'ge_pipe'), ('ge_objekt', 'ge_startPoint'), ('ge_objekt', 'ge_endPoint')]),
        ),
    ]
