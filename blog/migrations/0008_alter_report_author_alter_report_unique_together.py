# Generated by Django 4.2.7 on 2024-05-22 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0007_alter_report_author_alter_report_otherdescription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="report",
            unique_together={("post", "author")},
        ),
    ]
