# Generated by Django 5.0 on 2023-12-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0003_historicalperformance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.IntegerField(),
        ),
    ]
