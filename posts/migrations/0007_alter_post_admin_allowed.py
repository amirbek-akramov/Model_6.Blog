# Generated by Django 4.2 on 2024-01-28 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='admin_allowed',
            field=models.BooleanField(default=False),
        ),
    ]
