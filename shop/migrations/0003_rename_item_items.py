# Generated by Django 4.0.6 on 2022-08-04 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_product_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Items',
        ),
    ]