# Generated by Django 4.1.3 on 2023-01-07 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='general',
            fields=[
                ('Email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]
