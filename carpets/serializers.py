from rest_framework import serializers
from .models import Carpet, Color, Design, Length, Width, Radius

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['value']  

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = ['value']  

class LengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Length
        fields = ['value']  

class RadiusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radius
        fields = ['value']  

class WidthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width
        fields = ['value']  



class CarpetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        fields = '__all__'
