# Generated by Django 5.0.7 on 2024-08-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settingsapp', '0002_alter_social_links_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_links',
            name='link',
            field=models.URLField(unique=True),
        ),
    ]