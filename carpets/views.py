from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Carpet, Color, Design, Length, Radius, Width, Year, Month
from .serializers import CarpetSerializer, ColorSerializer, DesignSerializer, WidthSerializer, LengthSerializer, RadiusSerializer
from rest_framework.response import Response

class CarpetByColorView(generics.ListAPIView):
    serializer_class = CarpetSerializer

    def get_queryset(self):
        color = self.kwargs['color']
        return Carpet.objects.filter(rang__value=color)  # تغییر به rang

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
        return Carpet.objects.filter(naghsheh__value=design)  # تغییر به naghsheh

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

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Carpet, Year, Month
from .serializers import CarpetSerializer

class CarpetViewSet(viewsets.ViewSet):
    
    def list(self, request, year=None, month=None):
        """
        لیست کردن فرش‌ها براساس سال و ماه (اختیاری).
        """
        year_instance = get_object_or_404(Year, value=year)
        
        if month:
            month_instance = get_object_or_404(Month, year=year_instance, value=month)
            carpets = Carpet.objects.filter(carpet_month=month_instance)
        else:
            carpets = Carpet.objects.filter(carpet_month__year=year_instance)

        serializer = CarpetSerializer(carpets, many=True)
        return Response(serializer.data)

    def retrieve(self, request, year, month, pk=None):
        try:
            year_instance = Year.objects.filter(value=year).first()
            if not year_instance:
                return Response({'error': 'Year not found'}, status=404)
            
            month_instance = Month.objects.filter(year=year_instance, value=month).first()
            if not month_instance:
                return Response({'error': 'Month not found'}, status=404)
            
            carpet = Carpet.objects.filter(id=pk, month=month_instance).first()
            if not carpet:
                return Response({'error': 'Carpet not found'}, status=404)

            serializer = CarpetSerializer(carpet)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def create(self, request, year, month=None):
        """
        ایجاد یک فرش جدید.
        """
        year_instance = get_object_or_404(Year, value=year)
        
        if month:
            month_instance = get_object_or_404(Month, year=year_instance, value=month)
        else:
            month_instance = None

        serializer = CarpetSerializer(data=request.data)
        if serializer.is_valid():
            carpet = serializer.save()
            if month_instance:
                month_instance.carpets.add(carpet)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, year, month=None, pk=None):
        """
        به‌روزرسانی یک فرش.
        """
        year_instance = get_object_or_404(Year, value=year)

        if month:
            month_instance = get_object_or_404(Month, year=year_instance, value=month)
            carpet = get_object_or_404(Carpet, pk=pk, carpet_month=month_instance)
        else:
            carpet = get_object_or_404(Carpet, pk=pk, carpet_month__year=year_instance)

        serializer = CarpetSerializer(carpet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, year, month=None, pk=None):
        """
        حذف یک فرش.
        """
        year_instance = get_object_or_404(Year, value=year)

        if month:
            month_instance = get_object_or_404(Month, year=year_instance, value=month)
            carpet = get_object_or_404(Carpet, pk=pk, carpet_month=month_instance)
        else:
            carpet = get_object_or_404(Carpet, pk=pk, carpet_month__year=year_instance)

        carpet.delete()
        return Response(status=204)
