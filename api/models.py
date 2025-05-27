from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} - {self.booking_date}"
