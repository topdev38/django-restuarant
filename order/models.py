from django.db import models
from django.contrib.auth import get_user_model

from menu.models import Food, Alcohol

TABLES = [
    (1, 'TABLE 1'),
    (2, 'TABLE 2'),
    (3, 'TABLE 3'),
    (4, 'TABLE 4'),
    (5, 'TABLE 5'),
]


class Order(models.Model):
    order_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    table = models.CharField(max_length=7, choices=TABLES, default='TABLE 1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_by + ' ' + self.table
