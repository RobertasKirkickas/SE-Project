from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
# Create your models here.

CATEGORIES_choices = [
    ('RPG', 'RPG'),
    ('Fighting', 'Fighting'),
    ('Shooter', 'Shooter'),
    ('Action', 'Action'),
    ('Racing', 'Racing'),
    ('Adventure', 'Adventure'),
    ('Sports', 'Sports')
]



class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_title = models.CharField(max_length=64)
    game_genre = models.CharField(max_length=64)
    game_category = models.CharField(choices=CATEGORIES_choices, max_length=10)
    game_platform = models.CharField(max_length=64)
    game_price = models.DecimalField(max_digits=7, decimal_places=2)  
    game_quantity = models.IntegerField()
    game_discount_price = models.DecimalField(max_digits=7, decimal_places=2)  
    game_description = models.TextField()
    image_url = models.ImageField(upload_to='game-images/', default="game-images/default.png")
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.game_title)  # Automatically generate slug if not provided
        super().save(*args, **kwargs)

        games_without_slug = Games.objects.filter(slug='')

        for game in games_without_slug:
            game.slug = slugify(game.game_title)  # Generates a slug from the game title
            game.save()

    def __str__(self):
        return self.game_title
    
    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'slug':self.slug})

    # Testing unit
    def get_total_price(self):
        return self.game_price * self.game_quantity

    def clean(self):
        if self.game_price<0:
            raise ValidationError('Price can not be negative')
        if self.game_quantity<0:
            raise ValidationError('Quantity can not be negative')
        

# class Item(models.Model):
#     title = models.CharField(max_length=200)
#     price = models.IntegerField()
#     discount_price = models.IntegerField(blank=True, null=True)
#     slug = models.SlugField()

#     def __str__(self):
#         return self.title


# Shopping Order
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Games, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of  {self.item.game_title}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username