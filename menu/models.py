from django.db import models

LABEL_CHOICES = [
    ('RED', 'red'),
    ('BLUE', 'blue'),
    ('BLACK', 'black'),
]

class BaseMenu(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

class MenuCategory(models.Model):
    name = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Food(BaseMenu):
    calorie = models.IntegerField()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

class Alcohol(BaseMenu):
    percetage = models.IntegerField()
    label = models.CharField(max_length=5, choices=LABEL_CHOICES, default='RED')