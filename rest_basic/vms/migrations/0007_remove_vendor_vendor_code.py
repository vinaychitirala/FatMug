# Generated by Django 5.0 on 2023-12-09 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0006_alter_historicalperformance_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_code',
        ),
    ]
