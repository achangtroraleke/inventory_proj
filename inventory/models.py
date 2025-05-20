from django.db import models
from django.urls import reverse
# Create your models here.

class Container(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('container_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    container = models.ForeignKey(Container, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name