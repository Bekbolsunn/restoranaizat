from .serializers import FoodListSerializer, FoodDetailSerializer, ReviewSerializer
from .models import Food, Review
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions


class FoodListAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class FoodDetailAPIView(RetrieveUpdateDestroyAPIView):
    model = Food
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    lookup_field = 'id'


class ReviewAPIView(RetrieveUpdateDestroyAPIView):
    model = Review
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
