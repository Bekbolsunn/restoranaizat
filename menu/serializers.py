from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    food = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'image', 'price', 'name']


class FoodDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Food
        fields = '__all__'


# class FoodBasketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Basket
#         fields = 'all'
