# Generated by Django 4.2.19 on 2025-03-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0002_alter_games_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='image_url',
            field=models.ImageField(default='static/default.png', upload_to='static/'),
        ),
    ]
