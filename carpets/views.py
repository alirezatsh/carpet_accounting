from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Carpet, Color, Design, Length, Radius, Width
from .serializers import CarpetSerializer, ColorSerializer, DesignSerializer, WidthSerializer, LengthSerializer, RadiusSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *

class CarpetByColorView(generics.ListAPIView):
    serializer_class = CarpetSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]


    def get_queryset(self):
        color = self.kwargs['color']
        return Carpet.objects.filter(rang__value=color)  # تغییر به rang

class CarpetListView(generics.ListAPIView):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
class CarpetDetailView(generics.RetrieveAPIView):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]


class CarpetByDesignView(generics.ListAPIView):
    serializer_class = CarpetSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]
 

    def get_queryset(self):
        design = self.kwargs['design']
        return Carpet.objects.filter(naghsheh__value=design)  # تغییر به naghsheh

class ColorListView(generics.ListAPIView):  
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
class ColorDetailView(generics.RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
class DesignDetailView(generics.RetrieveAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
class DesignListView(generics.ListAPIView):  
    queryset = Design.objects.all()  
    serializer_class = DesignSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]


class LengthListView(generics.ListAPIView):
    queryset = Length.objects.all()
    serializer_class = LengthSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]


class WidthListView(generics.ListAPIView):
    queryset = Width.objects.all()
    serializer_class = WidthSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
class RadiusListView(generics.ListAPIView):
    queryset = Radius.objects.all()
    serializer_class = RadiusSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]




class CarpetViewSet(viewsets.ModelViewSet):
    
    """
    this is for viewing an editing the carpets
    """
    
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'فرش با موفقیت حذف شد'} , status=status.HTTP_200_OK)
