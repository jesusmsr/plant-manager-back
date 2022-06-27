from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from plant_app.api.serializers import PlantSerializer, PlantImageSerializer
from rest_framework import status
from datetime import datetime, timedelta
from plant_app.models import Plant
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser


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
        serializer = PlantSerializer(data=request.data)
        user = self.request.user
        if Plant.objects.filter(code=request.data['code']):
            return Response({'error': 'There is already a plant with that code'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid() :
                serializer.save(user=user)
                # imageSerializer = PlantImageSerializer(data=request.data['image'])
                # if imageSerializer.is_valid():
                #     imageSerializer.save(plant=serializer.validated_data)
                
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlantDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlantSerializer(plant, context={'request': request})
        return Response(serializer.data)
    
class PlantImageDetailAV(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, pk):
        
        file_serializer = PlantImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': file_serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)