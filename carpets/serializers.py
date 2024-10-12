from rest_framework import serializers
from .models import Carpet, Color, Design , Width , Length , Radius

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'
        
    
    
class SizeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Carpet
            fields = ['length', 'width', 'radius']
            
            
class LengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Length
        fields = '__all__'

class WidthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width
        fields = '__all__'
        
class RadiusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radius
        fields = '__all__'



class CarpetSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    design = DesignSerializer()
    width = WidthSerializer()
    length = LengthSerializer()
    
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     if instance.shape.value == 'rectangle':
    #         # حذف فیلد شعاع برای فرش‌های مستطیلی
    #         data.pop('radius')
    #     elif instance.shape.value == 'circle':
    #         # حذف فیلد طول و عرض برای فرش‌های دایره‌ای
    #         data.pop('length')
    #         data.pop('width')
    #     return data

    class Meta:
        model = Carpet
        fields = '__all__'