from rest_framework import serializers
from .models import Carpet, Color, Design, Width, Length , Radius

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
    rang = serializers.CharField(source='rang.value')  
    naghsheh = serializers.CharField(source='naghsheh.value')  
    tool = serializers.CharField(source='tool.value')  
    arz = serializers.CharField(source='arz.value')  

    class Meta:
        model = Carpet
        fields = ['id' , 'value', 'rang', 'naghsheh', 'tool', 'arz', 'isrectangle', 'metraj', 'serial', 'code',
                  'shirazeh', 'cheleh', 'gereh', 'shirazehkhoroug', 'chelehkhoroug', 'grehkhoroug',
                  'shirazehvouroud', 'chellehvouroud', 'gerehvouroud', 'ersalshodeh']

    def create(self, validated_data):
        rang_value = validated_data.pop('rang')['value']  
        naghsheh_value = validated_data.pop('naghsheh')['value']  
        tool_value = validated_data.pop('tool')['value']  
        arz_value = validated_data.pop('arz')['value']  
        rang_instance = Color.objects.get(value=rang_value)
        naghsheh_instance = Design.objects.get(value=naghsheh_value)
        tool_instance = Length.objects.get(value=tool_value)
        arz_instance = Width.objects.get(value=arz_value)
        carpet = Carpet.objects.create(
            **validated_data,
            rang=rang_instance,
            naghsheh=naghsheh_instance,
            tool=tool_instance,
            arz=arz_instance,
        )
        return carpet
