from django.contrib import admin
from .models import MenuCategory, Food, Alcohol

admin.site.register(MenuCategory)
admin.site.register(Food)
admin.site.register(Alcohol)