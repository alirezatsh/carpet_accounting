from rest_framework import serializers
from .models import Carpet, Color, Design, Length, Width, Radius
from accounts.models import Workers

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
    rang = serializers.CharField(required=False, allow_blank=True) 
    naghsheh = serializers.CharField(required=False, allow_blank=True)
    tool = serializers.CharField(required=False, allow_blank=True)
    arz = serializers.CharField(required=False, allow_blank=True)  
    shirazeh = serializers.CharField(required=False, allow_blank=True)
    cheleh = serializers.CharField(required=False, allow_blank=True)
    gereh = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Carpet
        fields = '__all__' 

    def create(self, validated_data):
        return Carpet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
