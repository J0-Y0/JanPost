# Generated by Django 4.2.7 on 2024-05-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_remove_report_name_report_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="otherDescription",
            field=models.TextField(verbose_name="Details"),
        ),
    ]
