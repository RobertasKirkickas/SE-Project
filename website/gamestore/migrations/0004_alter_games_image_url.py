# Generated by Django 5.1.5 on 2025-02-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0003_alter_games_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
