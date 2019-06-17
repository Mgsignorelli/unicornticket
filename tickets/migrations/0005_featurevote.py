# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-09 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0004_bugvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Feature', default=None,
                                   blank=True, null=True)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]