from rest_framework import serializers
from django.db.models import fields
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'genres')
