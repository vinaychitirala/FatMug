# Generated by Django 5.0 on 2023-12-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0022_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniquecode',
            name='code',
            field=models.IntegerField(),
        ),
    ]
