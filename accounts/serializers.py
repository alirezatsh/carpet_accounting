from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import Section, SectionUser , Workers , Help




class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(source='*')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_info']


class SectionUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SectionUser
        fields = ['user']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
    
class WorkerSerializer(serializers.ModelSerializer):
    section = serializers.StringRelatedField()

    class Meta:
        model = Workers
        fields = ['id', 'name', 'last_name', 'section']


    def get_section(self, obj):
        section_user = SectionUser.objects.filter(user=obj).first()
        if section_user:
            return section_user.section.value
        return None  
    
    
class WorkerSectionSerializer(serializers.ModelSerializer):
    section_name = serializers.CharField(source='section.value', write_only=True) 
    section = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Workers
        fields = ['id', 'name', 'last_name', 'section', 'section_name' , 'phone' , 'landline_phone' , 'address']  

    def create(self, validated_data):
        section_name = validated_data.pop('section').get('value')
        
        try:
            section = Section.objects.get(value=section_name)
        except Section.DoesNotExist:
            raise serializers.ValidationError(f"Section with name '{section_name}' does not exist.")
        
        # ایجاد کاربر جدید
        worker = Workers.objects.create(section=section, **validated_data)
        return worker

    def update(self, instance, validated_data):
        # به‌روزرسانی فیلدهای کاربر
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # دریافت نام بخش و پیدا کردن بخش
        section_name = validated_data.pop('section').get('value', None)
        if section_name:
            try:
                section = Section.objects.get(value=section_name)
                instance.section = section
            except Section.DoesNotExist:
                raise serializers.ValidationError(f"Section with name '{section_name}' does not exist.")
        
        instance.save()
        return instance



class HelpWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'




