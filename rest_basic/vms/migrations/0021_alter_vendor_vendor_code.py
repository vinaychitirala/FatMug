# Generated by Django 5.0 on 2023-12-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0020_purchaseorder_po_number_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
    ]
