# Generated by Django 4.0.6 on 2022-08-18 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_tracker_alter_checkout_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='CustomerEnteredOrderId',
        ),
    ]