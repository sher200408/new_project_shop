# Generated by Django 5.1.4 on 2025-01-07 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_bloghashtagmodel_alter_blogmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloghashtagmodel',
            options={'verbose_name': 'blog hashtag', 'verbose_name_plural': 'blogs hashtags'},
        ),
    ]
