from rest_framework import serializers
from plant_app.models import Plant, PlantImage

class PlantImageSerializer(serializers.ModelSerializer):
    image = serializers.FileField(read_only=False)
    class Meta:
        model = PlantImage
        fields = ['image']
        
class PlantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    image = PlantImageSerializer(read_only=True)
    class Meta:
        model = Plant
        fields = '__all__'
    