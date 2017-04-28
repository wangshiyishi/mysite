# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usermane', models.CharField(max_length=10, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=240, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
