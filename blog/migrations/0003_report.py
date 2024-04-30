# Generated by Django 4.2.7 on 2024-04-30 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Commented by')),
                ('type', models.CharField(choices=[('none_educational', 'None Educational'), ('ethnic', 'Ethnic Violence'), ('political', 'Political Content'), ('explicit', 'Explicit Content'), ('spam', 'looks a spam'), ('other', 'other')], max_length=50)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='blog.post')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
                'ordering': ('-published_date',),
            },
        ),
    ]
