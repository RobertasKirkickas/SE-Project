# Generated by Django 5.1.5 on 2025-02-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_sku', models.CharField(max_length=50, unique=True)),
                ('game_title', models.CharField(max_length=64)),
                ('game_genre', models.CharField(max_length=64)),
                ('game_platform', models.CharField(max_length=64)),
                ('game_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('game_quantity', models.IntegerField()),
                ('image_url', models.CharField(default='images/game-images/default.jpg', max_length=255)),
            ],
        ),
    ]
