# Generated by Django 4.2.7 on 2024-05-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
