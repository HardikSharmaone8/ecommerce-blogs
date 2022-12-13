# Generated by Django 4.0.6 on 2022-08-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_item_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='discription',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='items',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]
