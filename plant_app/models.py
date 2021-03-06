from operator import le
from django.db import models
from account_app.models import Account 

# Create your models here.
class Plant(models.Model):
    name = models.CharField(null=True,max_length=50)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="userPlant")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True,upload_to="images", default="/images/assets/default-plant.png")
    
    def __str__(self):
        return self.name
    
class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="plantImage")
    image = models.FileField(upload_to="images")
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.plant.name