# from django.contrib.auth.models import User
from gallery.models import Image, User
from rest_framework import serializers
from rest_framework.response import Response


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Image
        #fields =  'id', 'user', 'file'
        fields =  '__all__'


class ImageListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Image
        fields =  'file', 'user'


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = 'id', 'file'


class UserSerializer(serializers.ModelSerializer):
    # images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())
    # images = UserImageSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = 'id', 'email', 'password' 

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        new_user = User(email=email)
        new_user.is_active = True
        new_user.set_password(password)
        new_user.save()

        return new_user

