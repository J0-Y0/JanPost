# Generated by Django 5.0.4 on 2024-04-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Commented by'),
        ),
    ]
