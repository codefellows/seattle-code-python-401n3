from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=64)
    rating = models.IntegerField(max_length=10, default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name