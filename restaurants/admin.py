from django.contrib import admin
from .models import Restaurant, Category, FoodItem


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'is_available')
    list_filter = ('restaurant', 'is_available')


admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(FoodItem, FoodItemAdmin)
