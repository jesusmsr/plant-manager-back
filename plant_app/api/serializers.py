from rest_framework import serializers
from plant_app.models import Plant, PlantImage

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'
        
class PlantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    images = PlantImageSerializer(many=True, read_only=True)
    class Meta:
        model = Plant
        fields = '__all__'
    