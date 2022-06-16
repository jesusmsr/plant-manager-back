from rest_framework import serializers
from plant_app.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Plant
        fields = '__all__'