# Generated by Django 5.0.4 on 2024-04-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society', '0007_residentproblem_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residentproblem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
