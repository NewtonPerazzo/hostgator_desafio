# Generated by Django 3.1.7 on 2021-03-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210303_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominio',
            name='price',
            field=models.FloatField(blank=True, default=26.99, null=True),
        ),
        migrations.AlterField(
            model_name='dominio',
            name='reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]