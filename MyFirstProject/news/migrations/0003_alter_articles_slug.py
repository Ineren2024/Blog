# Generated by Django 5.0.4 on 2024-12-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_options_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
