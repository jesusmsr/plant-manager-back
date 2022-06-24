from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from plant_app.api.serializers import PlantSerializer, PlantImageSerializer
from rest_framework import status
from datetime import datetime, timedelta
from plant_app.models import Plant
from rest_framework.response import Response


class PlantAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if self.request.user.is_staff:
            bookings = Plant.objects.all()
        else:
            bookings = Plant.objects.filter(user=self.request.user)
        serializer = PlantSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlantSerializer(data=request.data['plant'])
        user = self.request.user
        if Plant.objects.filter(code=request.data['plant']['code']):
            return Response({'error': 'There is already a plant with that code'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid() :
                serializer.save(user=user)
                imageSerializer = PlantImageSerializer(data=request.data['image'])
                if imageSerializer.is_valid():
                    imageSerializer.save(plant=serializer.validated_data)
                
                return Response(imageSerializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        