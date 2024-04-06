# Generated by Django 5.0.4 on 2024-04-05 13:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('secretary_uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('resident_uid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
