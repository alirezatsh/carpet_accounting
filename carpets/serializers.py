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
    rang = serializers.CharField()
    naghsheh = serializers.CharField()
    tool = serializers.CharField()  # تغییر به CharField
    arz = serializers.CharField()    # تغییر به CharField
    shirazeh = serializers.PrimaryKeyRelatedField(queryset=Workers.objects.all())
    cheleh = serializers.PrimaryKeyRelatedField(queryset=Workers.objects.all())
    gereh = serializers.PrimaryKeyRelatedField(queryset=Workers.objects.all())

    class Meta:
        model = Carpet
        fields = '__all__'

    def create(self, validated_data):
        rang_value = validated_data.pop('rang')
        naghsheh_value = validated_data.pop('naghsheh')
        tool_value = validated_data.pop('tool')
        arz_value = validated_data.pop('arz')

        # تلاش برای رنگ
        rang_instance, created = Color.objects.get_or_create(value=rang_value)
        validated_data['rang'] = rang_instance

        # تلاش برای طرح
        naghsheh_instance, created = Design.objects.get_or_create(value=naghsheh_value)
        validated_data['naghsheh'] = naghsheh_instance

        # تلاش برای طول
        tool_instance, created = Length.objects.get_or_create(value=tool_value)
        validated_data['tool'] = tool_instance

        # تلاش برای عرض
        arz_instance, created = Width.objects.get_or_create(value=arz_value)
        validated_data['arz'] = arz_instance

        carpet = Carpet.objects.create(**validated_data)
        return carpet

    def get_rang(self, obj):
        return obj.rang.value if obj.rang else None

    def get_naghsheh(self, obj):
        return obj.naghsheh.value if obj.naghsheh else None
    
    def get_tool(self, obj):
        return obj.tool.value if obj.tool else None

    def get_arz(self, obj):
        return obj.arz.value if obj.arz else None
