# Generated by Django 4.0.6 on 2022-08-18 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_checkout_porductorderid_alter_checkout_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='PorductOrderId',
            new_name='OrderId',
        ),
    ]