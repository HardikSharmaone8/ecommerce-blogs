# Generated by Django 4.0.6 on 2022-08-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_publishblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishblog',
            name='Blog_Image',
            field=models.ImageField(default='', upload_to='shop/image'),
        ),
    ]
