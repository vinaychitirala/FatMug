# Generated by Django 5.0 on 2023-12-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0009_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.IntegerField(editable=False, null=True, unique=True),
        ),
    ]