import re
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from plant_app.api.serializers import PlantSerializer, PlantImageSerializer
from rest_framework import status
from datetime import datetime, timedelta
from plant_app.models import Plant
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
import json

class PlantAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if self.request.user.is_staff:
            plants = Plant.objects.all()
        else:
            plants = Plant.objects.filter(user=self.request.user)
        serializer = PlantSerializer(plants, many=True, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        
        user = self.request.user
        # if Plant.objects.filter(code=request.POST['code']):
        #     return Response({'error': 'There is already a plant with that code'}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        plant = Plant.objects.get(pk=pk)
        serializer = PlantSerializer(plant,data=request.data)
        if serializer.is_valid() :
            if len(request.FILES) > 0:
                serializer.save(user=user,image=request.FILES['image'])
            else:
                serializer.save(user=user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = PlantSerializer(data=request.POST)
        user = self.request.user
        if Plant.objects.filter(code=request.POST['code']):
            return Response({'error': 'There is already a plant with that code'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid() :
                if len(request.FILES) > 0:
                    serializer.save(user=user,image=request.FILES['image'])
                else:
                    serializer.save(user=user)
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
        plant = Plant.objects.get(pk=pk)
        file_serializer = PlantImageSerializer(data=request.FILES)
        if file_serializer.is_valid():
            file_serializer.image = request.FILES['image']
            file_serializer.save(plant=plant)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': file_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
