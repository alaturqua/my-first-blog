# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='yazar',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='yaratilis_tarihi',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='yayinlanma_tarihi',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='yazi',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='baslik',
            new_name='title',
        ),
    ]
