# Generated by Django 5.0 on 2023-12-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0010_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
