# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('photo', models.ImageField(upload_to=b'static/Blog_img', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('ccontent', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=b'350', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('author', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='blog.User')),
                ('blog', models.ForeignKey(verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2', to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='user',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usermane',
            new_name='username',
        ),
    ]
