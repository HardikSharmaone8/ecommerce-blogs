# Generated by Django 4.0.6 on 2022-08-04 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
