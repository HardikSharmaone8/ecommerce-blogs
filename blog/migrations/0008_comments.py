# Generated by Django 4.1 on 2022-08-27 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_publishblog_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Id', models.IntegerField()),
                ('Comment', models.TextField(max_length=500)),
                ('Commment_Date', models.DateTimeField(auto_now=True)),
                ('Parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comments')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.databaseblog')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL))
            ],
        ),
    ]