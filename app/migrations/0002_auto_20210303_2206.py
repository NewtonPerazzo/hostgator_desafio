# Generated by Django 3.1.7 on 2021-03-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominio',
            name='available',
            field=models.BooleanField(default=None),
        ),
    ]
