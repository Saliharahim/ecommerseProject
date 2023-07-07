from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    name=models.CharField(max_length=200)
    size=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images", null=True, blank=True)
    discription=models.CharField(max_length=200)

    
    def __str__(self) -> str:
        return self.name