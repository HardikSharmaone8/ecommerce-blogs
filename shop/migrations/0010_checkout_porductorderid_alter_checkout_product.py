# Generated by Django 4.0.6 on 2022-08-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_checkout_optionaladd_checkout_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='PorductOrderId',
            field=models.CharField(default='Order Id', max_length=100),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='Product',
            field=models.CharField(default='product name', max_length=100),
        ),
    ]