# Generated by Django 4.1 on 2022-08-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comments_reply_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Reply_id',
            field=models.CharField(max_length=500),
        ),
    ]