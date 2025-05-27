from django.contrib import admin
from .models import Category, MenuItem, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'featured']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'no_of_guests', 'booking_date']
    list_filter = ['booking_date']
    search_fields = ['name', 'user__username']
