# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 10:01

import uuid

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models
from swapper import get_model_name


class Migration(migrations.Migration):

    dependencies = [('topology', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                ('data', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=get_model_name('openwisp_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
                (
                    'topology',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='topology.Topology',
                    ),
                ),
            ],
            options={'abstract': False, 'verbose_name_plural': 'snapshots'},
        )
    ]
