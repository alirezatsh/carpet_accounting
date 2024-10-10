from django.shortcuts import render
from rest_framework import generics
from .models import Carpet , Color , Design , Shape , Length , Radius , Width
from .serializers import CarpetSerializer , ColorSerializer , DesignSerializer , WidthSerializer , LengthSerializer , RadiusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CarpetByColorView(generics.ListAPIView):
    serializer_class = CarpetSerializer

    def get_queryset(self):
        color = self.kwargs['color']
        return Carpet.objects.filter(color=color)
    

    
    
class CarpetListView(generics.ListAPIView):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer
    
class CarpetDetailView(generics.RetrieveAPIView):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer

class CarpetByDesignView(generics.ListAPIView):
    serializer_class = CarpetSerializer

    def get_queryset(self):
        design = self.kwargs['design']
        return Carpet.objects.filter(pattern=design) 
    
class ColorListView(generics.ListAPIView):  
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    
    
class ColorDetailView(generics.RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    

class DesignDetailView(generics.RetrieveAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    
class DesignListView(generics.ListAPIView):  
    queryset = Design.objects.all()  
    serializer_class = DesignSerializer

    
    
class LengthListView(generics.ListAPIView):
    queryset = Length.objects.all()
    serializer_class = LengthSerializer

class WidthListView(generics.ListAPIView):
    queryset = Width.objects.all()
    serializer_class = WidthSerializer
    
    
class RadiusListView(generics.ListAPIView):
    queryset = Radius.objects.all()
    serializer_class = RadiusSerializer