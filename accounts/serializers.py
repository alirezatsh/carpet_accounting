from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import Section, SectionUser , Workers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_password(self, value):
        # استفاده از اعتبارسنجی‌های پسورد جنگو
        try:
            validate_password(value)
        except ValidationError as e:
            # تبدیل خطاهای جنگو به خطاهای سازگار با DRF
            raise DRFValidationError(e.messages)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


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
    section = serializers.SerializerMethodField()

    class Meta:
        model = Workers
        fields = ['id', 'name', 'last_name', 'section']

    def get_section(self, obj):
        # پیدا کردن بخش مرتبط با هر کارگر
        section_user = SectionUser.objects.filter(user=obj).first()
        if section_user:
            return section_user.section.name  
        return None  
    
    
    
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import Section, SectionUser , Workers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_password(self, value):
        # استفاده از اعتبارسنجی‌های پسورد جنگو
        try:
            validate_password(value)
        except ValidationError as e:
            # تبدیل خطاهای جنگو به خطاهای سازگار با DRF
            raise DRFValidationError(e.messages)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


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
        # پیدا کردن بخش مرتبط با هر کارگر
        section_user = SectionUser.objects.filter(user=obj).first()
        if section_user:
            return section_user.section.name  
        return None  
    
    
class WorkerSectionSerializer(serializers.ModelSerializer):
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), required=False)

    class Meta:
        model = Workers
        fields = ['id', 'name', 'last_name', 'section']

    def create(self, validated_data):
        section = validated_data.pop('section', None)
        worker = Workers.objects.create(**validated_data)
        if section:
            worker.section = section
            worker.save()  # ذخیره نهایی بخش کارگر
        return worker

    def update(self, instance, validated_data):
        section = validated_data.pop('section', None)
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if section:
            instance.section = section  # بخش جدید را به کارگر نسبت می‌دهیم
        instance.save()
        return instance






