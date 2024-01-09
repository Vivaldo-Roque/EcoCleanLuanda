# Generated by Django 5.0 on 2024-01-09 09:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentorLixo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=100)),
                ('geolocalizacao', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'contentorerslixo',
                'db_table': 'contentores_lixo',
                'managed': True,
            },
        ),
    ]
