# Generated by Django 5.1.1 on 2024-09-13 08:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0007_article_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
