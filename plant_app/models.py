from operator import le
from django.db import models
from account_app.models import Account 

# Create your models here.
class Plant(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="userPlant")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code
    
class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="plantImage")
    image = models.ImageField(upload_to="images")
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.plant.name