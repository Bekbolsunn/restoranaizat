from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/foods/review/<int:id>/', views.ReviewAPIView.as_view()),
    path('api/v1/foods/', views.FoodListAPIView.as_view()),
    path('api/v1/foods/<int:id>/', views.FoodDetailAPIView.as_view())
]
