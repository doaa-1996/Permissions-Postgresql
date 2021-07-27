from django.urls import path
from .views import MealListView, MealDetailsView
urlpatterns = [
    path('', MealListView.as_view(), name='Meal_api'),
    path('<int:pk>', MealDetailsView.as_view(), name='Meal_details_api'),


]