from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    img=models.TextField()
    country=models.CharField(max_length=64)
    def __str__(self):
        return self.title