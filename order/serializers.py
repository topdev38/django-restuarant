from rest_framework import serializers
from .models import Order
import datetime


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.food = validated_data.get('food', instance.food)
        instance.alcohol = validated_data.get('alcohol', instance.alcohol)
        instance.table = validated_data.get('table', instance.table)
        instance.updated_at = datetime.datetime.now()
        return instance
