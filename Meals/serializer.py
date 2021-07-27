from rest_framework import serializers
from .models import Post


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description',
                  'created_at', 'author', 'img', 'country')
        model = Post