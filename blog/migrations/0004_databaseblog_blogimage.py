# Generated by Django 4.0.6 on 2022-08-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blog_author_databaseblog_blogauthor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseblog',
            name='BlogImage',
            field=models.ImageField(default='', upload_to='shop/image'),
        ),
    ]