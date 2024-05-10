# Generated by Django 4.2.7 on 2024-05-04 22:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_post_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorite',
        ),
        migrations.AddField(
            model_name='post',
            name='favorite',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
