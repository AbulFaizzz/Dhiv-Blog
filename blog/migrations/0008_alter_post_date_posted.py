# Generated by Django 5.0.6 on 2024-06-18 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_options_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 6, 49, 39, 305839, tzinfo=datetime.timezone.utc)),
        ),
    ]