# Generated by Django 4.1 on 2022-08-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comments_reply_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Reply_id',
            field=models.IntegerField(),
        ),
    ]
