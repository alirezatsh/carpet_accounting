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
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), required=True)

    class Meta:
        model = Workers
        fields = ['id', 'name', 'last_name', 'section']

    def create(self, validated_data):
        # Validate section
        section = validated_data.get('section')
        if section is None:
            raise serializers.ValidationError("Section ID must be provided.")
        
        # Create worker
        worker = Workers.objects.create(**validated_data)
        return worker

    def update(self, instance, validated_data):
        # Update fields
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Validate section
        section = validated_data.get('section')
        if section is not None:
            instance.section = section
        
        instance.save()
        return instance


class HelpWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'




